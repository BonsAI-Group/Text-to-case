from pydantic import BaseModel

from models.FormItem import FormItem


class FieldSubmit(BaseModel):
    context: str
    field: FormItem