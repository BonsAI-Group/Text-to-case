from typing import Tuple
from .IQuestionAnswerer import IQuestionAnswerer
from .QuestionAnswerModel import QuestionAnswerModel


class BertLargeSingleModelQuestionAnswerer(IQuestionAnswerer):
    """A Question Answering model that uses a single BERT Large model."""
    def __init__(self):
        self.model = QuestionAnswerModel("https://bert-large-uncased-who-1gsmt1ib.westeurope.inference.ml.azure.com/score")

    def answerQuestion(self, question: str, context: str) -> Tuple[str, float]:
        """Answer a question given a context. Returns the answer and the confidence.""" 
        return self.model.answerQuestion(question, context)
    