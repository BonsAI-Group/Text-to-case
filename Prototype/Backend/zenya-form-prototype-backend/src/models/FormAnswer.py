from pydantic import BaseModel

from .FieldAnswer import FieldAnswer

class FormAnswer(BaseModel):
    answers: dict[str, FieldAnswer] # The answers to the form fields, keyed by field name