from ml.BertLargeSingleModelQuestionAnswerer import BertLargeSingleModelQuestionAnswerer
from ml.IQuestionGenerator import IQuestionGenerator
from ml.IQuestionAnswerer import IQuestionAnswerer
from ml.InterrogativeQuestionGenerator import InterrogativeQuestionGenerator
from models.FieldAnswer import FieldAnswer
from models.FormItem import FormItem



class FieldService:
    """Service for handling fields."""
    def __init__(self):
        self.QuestionGenerator: IQuestionGenerator = InterrogativeQuestionGenerator()
        self.QuestionAnswerer: IQuestionAnswerer = BertLargeSingleModelQuestionAnswerer()

    def fillInField(self, field: FormItem, context: str) -> FieldAnswer:
        """Fill in a field."""
        # Generate question
        question = self.QuestionGenerator.generateQuestion(context, field.fieldName)
        # Answer question
        answer, confidence = self.QuestionAnswerer.answerQuestion(question, context)
        # Return answer
        return FieldAnswer(fieldName=field.fieldName, answer=answer, confidence=confidence)
    
    def fillInQuestionField(self, field: FormItem, context: str) -> FieldAnswer:
        """Fill in a question field."""
        # Answer question
        answer, confidence = self.QuestionAnswerer.answerQuestion(field.fieldName, context)
        # Return answer
        return FieldAnswer(fieldName=field.fieldName, answer=answer, confidence=confidence)