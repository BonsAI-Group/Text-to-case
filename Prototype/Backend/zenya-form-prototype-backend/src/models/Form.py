from typing import List
from pydantic import BaseModel

from .FormItem import FormItem

class Form(BaseModel):
    name: str # The name of the form
    fields: List[FormItem] # The form fields
