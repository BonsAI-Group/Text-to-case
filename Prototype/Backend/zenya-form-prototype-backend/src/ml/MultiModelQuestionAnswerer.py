from typing import Tuple

from models.Answer import Answer
from .IQuestionAnswerer import IQuestionAnswerer
from .QuestionAnswerModel import QuestionAnswerModel

from sentence_transformers import SentenceTransformer, util
import numpy as np



class MultiModelQuestionAnswerer(IQuestionAnswerer):
    def __init__(self):
        self.modelNames = {
            "deberta": "deepset/deberta-v3-large-squad2",
            # "distilbert": "distilbert-base-cased-distilled-squad",
            "bert_large": "deepset/bert-large-uncased-whole-word-masking-squad2",
            # "bert_base": "deepset/bert-base-cased-squad2",
            "roberta": "deepset/roberta-base-squad2"
        }
        self.models = {}
        for modelName in self.modelNames:
            self.models[modelName] = QuestionAnswerModel(self.modelNames[modelName])

        self.similarityModel = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

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

        averageConfidence = np.average([answers[modelName][1] for modelName in answers])

        for modelName in answers:
            print(modelName, answers[modelName])

        answer = Answer(answer=answers[closestAnswer][0], confidence=averageConfidence, isTrusted=True)
        return answer