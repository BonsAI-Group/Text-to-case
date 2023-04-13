from typing import Tuple
from .IQuestionAnswerer import IQuestionAnswerer
from .QuestionAnswerModel import QuestionAnswerModel

from sentence_transformers import SentenceTransformer, util
import numpy as np
from threading import Thread

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

    def getQuestionAnswerResult(self, modelName: str):
        result = QuestionAnswerModel(self.modelNames[modelName])
        self.models[modelName] = result

    def answerQuestion(self, question: str, context: str) -> Tuple[str, float]:
        """Answer a question given a context. Returns the answer and the confidence."""
        answers = {}
        for modelName in self.models:
            answers[modelName] = self.models[modelName].answerQuestion(question, context)

        embeddings = {}
        for modelName in answers:
            embeddings[modelName] = self.similarityModel.encode(answers[modelName][0])

        averageVector = np.average(list(embeddings.values()), axis=0)

        closestAnswer = max(answers, key=lambda k: util.pytorch_cos_sim(embeddings[k], averageVector))

        averageConfidence = np.average([answers[modelName][1] for modelName in answers])

        for modelName in answers:
            print(modelName, answers[modelName])

        return answers[closestAnswer][0], averageConfidence