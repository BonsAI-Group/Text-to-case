from ml.DestilbertBaseUncasedMnli import DestilbertBaseSingleModelMultiChoice
from ml.MultiModelQuestionAnswerer import MultiModelQuestionAnswerer
from ml.IQuestionGenerator import IQuestionGenerator
from ml.IQuestionAnswerer import IQuestionAnswerer
from ml.IMultiChoiceModel import IMultiChoiceModel
from ml.IRadioButtonModel import IRadioButtonModel
from ml.InterrogativeQuestionGenerator import InterrogativeQuestionGenerator
from models.FieldAnswer import FieldAnswer
from models.FormItem import FormItem
from enums.FieldType import FieldType
from ml.QuestionGenerator import QuestionGenerator
from models.FieldAnswer import FieldAnswer
from models.FormItem import FormItem
from models.Answer import Answer
from models.MultiAnswer import MultiAnswer
from ml.InterrogativeQuestionGenerator import InterrogativeQuestionGenerator
from ml.TextToNum import TextToNum
from ml.ITextToNum import ITextToNum
from ml.IDateTimeConverter import IDateTimeConverter
from ml.DateTimeConverter import DateTimeConverter
import datetime

class FieldService:
    """Service for handling fields."""
    def __init__(self):
        # self.QuestionGenerator: IQuestionGenerator = QuestionGenerator(formName)
        self.QuestionGenerator: IQuestionGenerator = InterrogativeQuestionGenerator()
        self.QuestionAnswerer: IQuestionAnswerer = MultiModelQuestionAnswerer()
        self.MultiChoiceModel: IMultiChoiceModel = DestilbertBaseSingleModelMultiChoice()
        self.RadioButtonModel: IRadioButtonModel = DestilbertBaseSingleModelMultiChoice()
        self.TextToNum: ITextToNum = TextToNum()
        self.DateTimeConverter: IDateTimeConverter = DateTimeConverter() 

    def fillInField(self, field: FormItem, context: str) -> FieldAnswer:
        """Fill in a field."""
        """Checking the field Type"""
        if field.fieldType == FieldType.TEXT:
            # Generate question
            question = self.QuestionGenerator.generateQuestion(context, field.fieldName)
            # Answer question
            answer: Answer = self.QuestionAnswerer.answerQuestion(question, context)
            # Return answer
            return FieldAnswer(fieldName=field.fieldName, answer=[answer.answer], confidence=[answer.confidence], isTrusted=[answer.isTrusted])
        elif field.fieldType == FieldType.NUMERIC:
            print(field.fieldName)
            # Generate question
            question = self.QuestionGenerator.generateQuestion(context, field.fieldName)
            # Answer question
            answer: Answer = self.QuestionAnswerer.answerQuestion(question, context)
            # Convert datatype
            numeric_answer = self.TextToNum.textToNum(answer.answer)
            return FieldAnswer(fieldName=field.fieldName, answer=[numeric_answer], confidence=[answer.confidence], isTrusted=[answer.isTrusted])
        elif field.fieldType == FieldType.MULTI_SELECT:
            # Testing Multi-Choice
            print("Multiple Choice")
            multi_choice: MultiAnswer = self.MultiChoiceModel.answerMultiChoice(context, field.params)
            return FieldAnswer(fieldName=field.fieldName, answer=multi_choice.answers, confidence=multi_choice.confidence, isTrusted=multi_choice.isTrusted)
        elif field.fieldType == FieldType.RADIO_BUTTON:
            radio_button: Answer = self.RadioButtonModel.answerRadioButton(context, field.params)
            # Return answer
            return FieldAnswer(fieldName=field.fieldName, answer=[radio_button.answer], confidence=[radio_button.confidence], isTrusted=[radio_button.isTrusted])
        elif field.fieldType == FieldType.DATE:
            question = self.QuestionGenerator.generateQuestion(context, field.fieldName)
            answer: Answer = self.QuestionAnswerer.answerQuestion(question, context)
            date_str = answer.answer
            date = self.DateTimeConverter.convertDate(date_str)
            # If the date could not be converted, return an empty answer. TODO: Maybe handle this better?
            if date is None:
                return FieldAnswer(fieldName=field.fieldName, answer=[], confidence=[answer.confidence], isTrusted=[False])
            date = date.isoformat()
            return FieldAnswer(fieldName=field.fieldName, answer=[date], confidence=[answer.confidence], isTrusted=[answer.isTrusted])
        elif field.fieldType == FieldType.TIME:
            question = self.QuestionGenerator.generateQuestion(context, field.fieldName)
            answer: Answer = self.QuestionAnswerer.answerQuestion(question, context)
            time_str = answer.answer
            time = self.DateTimeConverter.convertTime(time_str)
            # If the time could not be converted, return an empty answer. TODO: Maybe handle this better?
            if time is None:
                return FieldAnswer(fieldName=field.fieldName, answer=[], confidence=[answer.confidence], isTrusted=[False])
            time = time.isoformat()
            return FieldAnswer(fieldName=field.fieldName, answer=[time], confidence=[answer.confidence], isTrusted=[answer.isTrusted])
        elif field.fieldType == FieldType.DATE_TIME:
            question = self.QuestionGenerator.generateQuestion(context, field.fieldName)
            answer: Answer = self.QuestionAnswerer.answerQuestion(question, context)
            date_time_str = answer.answer
            date_time = self.DateTimeConverter.convertDateTime(date_time_str)
            # If the date time could not be converted, return an empty answer. TODO: Maybe handle this better?
            if date_time is None:
                return FieldAnswer(fieldName=field.fieldName, answer=[], confidence=[answer.confidence], isTrusted=[False])
            date_time = date_time.isoformat()
            return FieldAnswer(fieldName=field.fieldName, answer=[date_time], confidence=[answer.confidence], isTrusted=[answer.isTrusted])
    
    def fillInQuestionField(self, field: FormItem, context: str) -> FieldAnswer:
        """Fill in a question field."""
        # Answer question
        answer: Answer = self.QuestionAnswerer.answerQuestion(field.question, context)
        # Return answer
        return FieldAnswer(fieldName=field.fieldName, answer=answer.answer, confidence=answer.confidence, isTrusted=answer.isTrusted)