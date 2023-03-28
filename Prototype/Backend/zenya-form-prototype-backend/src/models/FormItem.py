from pydantic import BaseModel

class FormItem(BaseModel):
    fieldName: str