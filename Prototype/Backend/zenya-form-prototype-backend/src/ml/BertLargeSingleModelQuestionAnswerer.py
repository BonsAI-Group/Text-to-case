from .IQuestionAnswerer import IQuestionAnswerer
from .QuestionAnswerModel import QuestionAnswerModel


class BertLargeSingleModelQuestionAnswerer(IQuestionAnswerer):
    """A Question Answering model that uses a single BERT Large model."""
    def __init__(self):
        self.model = QuestionAnswerModel("bert-large-uncased-whole-word-masking-finetuned-squad")

    def answerQuestion(self, question: str, context: str) -> tuple[str, float]:
        """Answer a question given a context. Returns the answer and the confidence.""" 
        return self.model.answerQuestion(question, context)
    