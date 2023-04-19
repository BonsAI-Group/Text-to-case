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



class FieldService:
    """Service for handling fields."""
    def __init__(self):
        self.QuestionGenerator: IQuestionGenerator = InterrogativeQuestionGenerator()
        self.QuestionAnswerer: IQuestionAnswerer = MultiModelQuestionAnswerer()
        self.MultiChoiceModel: IMultiChoiceModel = DestilbertBaseSingleModelMultiChoice()
        self.RadioButtonModel: IRadioButtonModel = DestilbertBaseSingleModelMultiChoice()

    def fillInField(self, field: FormItem, context: str) -> FieldAnswer:
        """Fill in a field."""
        """Checking the field Type"""
        if field.fieldType == FieldType.TEXT:
            # Generate question
            question = self.QuestionGenerator.generateQuestion(context, field.fieldName)
            # Answer question
            answer, confidence = self.QuestionAnswerer.answerQuestion(question, context)
            # Return answer
            return FieldAnswer(fieldName=field.fieldName, answer=[answer], confidence=[confidence])
        elif field.fieldType == FieldType.MULTI_SELECT:
            # Testing Multi-Choice
            print("Multiple Choice")
            multi_choice = self.MultiChoiceModel.answerMultiChoice(context, field.params)

            # TODO: This is a temporary threshold.
            threshold = 0.0 
            answers = [multi_choice.labels[i] for i in range(len(multi_choice.labels)) if multi_choice.confidences[i] > threshold]
            confidences = [multi_choice.confidences[i] for i in range(len(multi_choice.confidences)) if multi_choice.confidences[i] > threshold]
            # Return answer
            return FieldAnswer(fieldName=field.fieldName, answer=answers, confidence=confidences)
        elif field.fieldType == FieldType.RADIO_BUTTON:
            radio_button = self.RadioButtonModel.answerRadioButton(context, field.params)
            # Return answer
            return FieldAnswer(fieldName=field.fieldName, answer=[radio_button[1][0]], confidence=[radio_button[2][0]])
    
    def fillInQuestionField(self, field: FormItem, context: str) -> FieldAnswer:
        """Fill in a question field."""
        # Answer question
        answer, confidence = self.QuestionAnswerer.answerQuestion(field.fieldName, context)
        # Return answer
        return FieldAnswer(fieldName=field.fieldName, answer=answer, confidence=confidence)