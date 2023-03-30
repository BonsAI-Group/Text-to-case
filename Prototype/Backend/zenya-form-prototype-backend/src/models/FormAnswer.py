from typing import Dict
from pydantic import BaseModel

from .FieldAnswer import FieldAnswer

class FormAnswer(BaseModel):
    answers: Dict[str, FieldAnswer] # The answers to the form fields, keyed by field name