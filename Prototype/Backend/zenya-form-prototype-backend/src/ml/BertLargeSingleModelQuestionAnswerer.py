from typing import Tuple

from models.Answer import Answer
from .IQuestionAnswerer import IQuestionAnswerer
from .QuestionAnswerModel import QuestionAnswerModel


class BertLargeSingleModelQuestionAnswerer(IQuestionAnswerer):
    """A Question Answering model that uses a single BERT Large model."""
    def __init__(self):
        self.model = QuestionAnswerModel("https://bert-large-uncased-who-1gsmt1ib.westeurope.inference.ml.azure.com/score")

    def answerQuestion(self, question: str, context: str) -> Answer:
        """Answer a question given a context. Returns the answer and the confidence.""" 
        answer, confidence = self.model.answerQuestion(question, context)
        return Answer(answer=answer, confidence=confidence, isTrusted=True)
    