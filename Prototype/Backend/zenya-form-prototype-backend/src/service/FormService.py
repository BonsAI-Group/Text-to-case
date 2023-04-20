from dto.FormSubmit import FormSubmit
from models.FormAnswer import FormAnswer
from service.FieldService import FieldService


class FormService:
    """Service for form operations."""

    def __init__(self, formName: str):
        self.fieldService: FieldService = FieldService(formName)

    def fillForm(self, formSubmit: FormSubmit) -> FormAnswer:
        """Fill a form given a form submit."""
        answers = {}
        for field in formSubmit.form.fields:
            answers[field.fieldName] = self.fieldService.fillInField(field, formSubmit.context)
        return FormAnswer(answers=answers)
    
    def fillQuestionForm(self, formSubmit: FormSubmit) -> FormAnswer:
        """Fill a question form given a form submit."""
        answers = {}
        for field in formSubmit.form.fields:
            answers[field.fieldName] = self.fieldService.fillInQuestionField(field, formSubmit.context)
        return FormAnswer(answers=answers)