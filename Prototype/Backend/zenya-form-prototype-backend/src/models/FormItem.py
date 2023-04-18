from pydantic import BaseModel
from typing import Optional

from enums.FieldType import FieldType


class FormItem(BaseModel):
    fieldName: str
    fieldType: FieldType
    params: Optional[list]