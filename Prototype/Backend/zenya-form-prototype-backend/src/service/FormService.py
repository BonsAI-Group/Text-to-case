from dto.FormSubmit import FormSubmit
from models.FormAnswer import FormAnswer
from service.FieldService import FieldService
from models.Form import Form
from service.FormRequesterService import FormRequesterService
from util.ZenyaFormParser import ZenyaFormParser


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
    
    def getAllForms(self) -> list[Form]:
        """Get all forms."""
        allForms = FormRequesterService.getAllForms()
        allFormsRequested = []
        for form in allForms:
            if len(allFormsRequested) >= 10:
                break
            try:
                requestedForm = FormRequesterService.getFormById(form["form_id"])
                allFormsRequested.append(requestedForm)
            except:
                pass
        return ZenyaFormParser.parseFormList(allFormsRequested)
        