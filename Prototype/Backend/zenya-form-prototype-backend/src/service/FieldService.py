from ml.BertLargeSingleModelQuestionAnswerer import BertLargeSingleModelQuestionAnswerer
from ml.MultiModelQuestionAnswerer import MultiModelQuestionAnswerer
from ml.IQuestionGenerator import IQuestionGenerator
from ml.IQuestionAnswerer import IQuestionAnswerer
from ml.QuestionGenerator import QuestionGenerator
from models.FieldAnswer import FieldAnswer
from models.FormItem import FormItem
from models.Answer import Answer



class FieldService:
    """Service for handling fields."""
    def __init__(self):
        self.QuestionGenerator: IQuestionGenerator = QuestionGenerator("Lunch")
        self.QuestionAnswerer: IQuestionAnswerer = MultiModelQuestionAnswerer()

    def fillInField(self, field: FormItem, context: str) -> FieldAnswer:
        """Fill in a field."""
        # Generate question
        question = self.QuestionGenerator.generateQuestion(field.fieldName)
        # Answer question
        answer: Answer = self.QuestionAnswerer.answerQuestion(question, context)
        # Return answer
        return FieldAnswer(fieldName=field.fieldName, answer=answer.answer, confidence=answer.confidence, isTrusted=answer.isTrusted)
    
    def fillInQuestionField(self, field: FormItem, context: str) -> FieldAnswer:
        """Fill in a question field."""
        # Answer question
        answer: Answer = self.QuestionAnswerer.answerQuestion(field.question, context)
        # Return answer
        return FieldAnswer(fieldName=field.fieldName, answer=answer.answer, confidence=answer.confidence, isTrusted=answer.isTrusted)