from ml.DestilbertBaseUncasedMnli import DestilbertBaseSingleModelMultiChoice
from ml.MultiModelQuestionAnswerer import MultiModelQuestionAnswerer
from ml.IQuestionGenerator import IQuestionGenerator
from ml.IQuestionAnswerer import IQuestionAnswerer
from ml.IMultiChoiceModel import IMultiChoiceModel
from ml.IRadioButtonModel import IRadioButtonModel
from ml.InterrogativeQuestionGenerator import InterrogativeQuestionGenerator
from models.FieldAnswer import FieldAnswer
from models.FormItem import FormItem



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
        if field.formType == "Normal":
            # Generate question
            question = self.QuestionGenerator.generateQuestion(context, field.fieldName)
            # Answer question
            answer, confidence = self.QuestionAnswerer.answerQuestion(question, context)
            # Return answer
            return FieldAnswer(fieldName=field.fieldName, answer=answer, confidence=confidence)
        elif field.formType == "MultiChoice":
            # Testing Multi-Choice
            print("Multiple Choice")
            multi_choice = self.MultiChoiceModel.answerMultiChoice(context, field.params)
            print(multi_choice)
            print(type(multi_choice))
            print(multi_choice[1])
            # Return answer
            return FieldAnswer(fieldName=field.fieldName, answer=multi_choice[1][0], confidence=multi_choice[2][0])
        elif field.formType == "RadioButton":
            print("Radio Button")
            radio_button = self.RadioButtonModel.answerRadioButton(context, field.params)
            print(radio_button)
            print(type(radio_button))
            print(radio_button[1])
            # Return answer
            return FieldAnswer(fieldName=field.fieldName, answer=radio_button[1][0], confidence=radio_button[2][0])
    
    def fillInQuestionField(self, field: FormItem, context: str) -> FieldAnswer:
        """Fill in a question field."""
        # Answer question
        answer, confidence = self.QuestionAnswerer.answerQuestion(field.fieldName, context)
        # Return answer
        return FieldAnswer(fieldName=field.fieldName, answer=answer, confidence=confidence)