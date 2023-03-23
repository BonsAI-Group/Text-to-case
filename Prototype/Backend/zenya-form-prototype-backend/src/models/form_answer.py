from pydantic import BaseModel

from .form_item import FormItem

class FormAnswer(BaseModel):
    answers: dict[str, str] # key value pair, where key is the name of the field and value is the generated answer