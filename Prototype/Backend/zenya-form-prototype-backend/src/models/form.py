from pydantic import BaseModel

from .FormItem import FormItem

class Form(BaseModel):
    name: str # The name of the form
    fields: list[FormItem] # The form fields