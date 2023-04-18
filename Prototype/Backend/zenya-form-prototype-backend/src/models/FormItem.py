from pydantic import BaseModel
from typing import Optional


class FormItem(BaseModel):
    fieldName: str
    formType: str
    params: Optional[list]