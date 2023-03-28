from ..ml.BertLargeSingleModelQuestionAnswerer import BertLargeSingleModelQuestionAnswerer
from ..ml.IQuestionGenerator import IQuestionGenerator
from ..ml.QuestionAnswerModel import QuestionAnswerModel
from ..models.FieldAnswer import FieldAnswer
from ..models.FormItem import FormItem


class FieldService:
    """Service for handling fields."""
    def __init__(self):
        self.QuestionGenerator: IQuestionGenerator = None # TODO: Implement question generator
        self.QuestionAnswerer: QuestionAnswerModel = BertLargeSingleModelQuestionAnswerer()

    def fillInField(self, field: FormItem, context: str) -> FieldAnswer:
        """Fill in a field."""
        # Generate question
        question = self.QuestionGenerator.generateQuestion(field.fieldName)
        # Answer question
        answer, confidence = self.QuestionAnswerer.answerQuestion(field.fieldName, context)
        # Return answer
        return FieldAnswer(fieldName=field.fieldName, answer=answer, confidence=confidence)
    
    def fillInQuestionField(self, field: FormItem, context: str) -> FieldAnswer:
        """Fill in a question field."""
        # Answer question
        answer, confidence = self.QuestionAnswerer.answerQuestion(field.fieldName, context)
        # Return answer
        return FieldAnswer(fieldName=field.fieldName, answer=answer, confidence=confidence)