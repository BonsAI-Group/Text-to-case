from typing import Dict, Tuple

from models.Answer import Answer
from .IQuestionAnswerer import IQuestionAnswerer
from .QuestionAnswerModel import QuestionAnswerModel

from sentence_transformers import SentenceTransformer, util
import numpy as np
from threading import Thread
import tensorflow as tf
from tensorflow import keras

class MultiModelQuestionAnswerer(IQuestionAnswerer):
    def __init__(self):
        self.modelNames = {
            "deberta": "https://bert-large-uncased-who-1gsmt1ib.westeurope.inference.ml.azure.com/score",
            # "deberta": "deepset/deberta-v3-large-squad2",
            # # "distilbert": "distilbert-base-cased-distilled-squad",
            "bert_large": "https://bert-large-uncased-who-1gsmt1ib.westeurope.inference.ml.azure.com/score",
            # "bert_large": "deepset/bert-large-uncased-whole-word-masking-squad2",
            # # "bert_base": "deepset/bert-base-cased-squad2",
            # "roberta": "deepset/roberta-base-squad2",
            "roberta": "https://bert-large-uncased-who-1gsmt1ib.westeurope.inference.ml.azure.com/score"
        }
        self.models = {}
        self.threads = [None] * len(self.modelNames)
        
        for i, modelName in enumerate(self.modelNames):
            self.threads[i] = Thread(target=self.getQuestionAnswerResult, args=(modelName,))
            self.threads[i].start()

        for i, modelName in enumerate(self.modelNames):
            self.threads[i].join()

        self.similarityModel = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

        self.trustModel = keras.models.load_model('../models/trust_model.keras')

        self.TRUST_THRESHOLD = 0.72

    def answerQuestion(self, question: str, context: str) -> Answer:
        """Answer a question given a context. Returns the answer and the confidence."""
        answers = {}
        for modelName in self.models:
            answers[modelName] = self.models[modelName].answerQuestion(question, context)

        embeddings = {}
        for modelName in answers:
            embeddings[modelName] = self.similarityModel.encode(answers[modelName][0])

        averageVector = np.average(list(embeddings.values()), axis=0)

        closestAnswer = max(answers, key=lambda k: util.pytorch_cos_sim(embeddings[k], averageVector))
        
        metrics = self.calculateMetrics(answers, embeddings, closestAnswer)

        isTrusted, confidence = self.trustAnswer(metrics)

        answer = Answer(answer=answers[closestAnswer][0], confidence=confidence, isTrusted=isTrusted)
        return answer
    
    def calculateMetrics(self, answers: Dict[str, Tuple[str, float]], embeddings: Dict[str, np.array], averageModel: str) -> Dict[str, float]:
        return_data = {}
        averageVector = np.average(list(embeddings.values()), axis=0)
        # Distance between the average vector and the vector of chosen answer
        return_data['final_answer_distance_to_average'] = util.pytorch_cos_sim(averageVector, embeddings[averageModel]).item()
        # Average distance between the average vector and the vectors of all answers
        return_data['mean_all_distances_to_average'] = np.mean([util.pytorch_cos_sim(averageVector, embeddings[model]).item() for model in embeddings]).item()
        # Average distance between all answers
        return_data['mean_distance_between_all_answers'] = np.mean([util.pytorch_cos_sim(embeddings[model1], embeddings[model2]).item() for model1 in embeddings for model2 in embeddings if model1 != model2]).item()
        # Average confidence of all models
        return_data['mean_confidence'] = np.mean([answers[modelName][1] for modelName in answers]).item()
        # Confidence of the chosen answer
        return_data['confidence_of_final_answer'] = answers[averageModel][1]
        # Number of models that returned the same answer as the chosen answer
        return_data['count_of_models_that_returned_the_same_answer'] = len([modelName for modelName in answers if answers[modelName][0] == answers[averageModel][0]])
        return return_data
    
    def trustAnswer(self, metrics: Dict[str, float]) -> Tuple[bool, float]:
        predictions = self.trustModel.predict(np.array([list(metrics.values())]), verbose=0)

        confidenceZero = predictions[0][0]
        confidenceOne = predictions[0][1]

        return confidenceOne > self.TRUST_THRESHOLD, confidenceOne