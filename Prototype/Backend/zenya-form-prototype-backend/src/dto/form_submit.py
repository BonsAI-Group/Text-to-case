from ..models.form import Form
from pydantic import BaseModel

class FormSubmit(BaseModel):
    context: str
    form: Form