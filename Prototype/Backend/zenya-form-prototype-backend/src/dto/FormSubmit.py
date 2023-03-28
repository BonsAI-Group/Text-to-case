from ..models.Form import Form
from pydantic import BaseModel

class FormSubmit(BaseModel):
    context: str
    form: Form