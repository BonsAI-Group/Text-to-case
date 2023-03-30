from pydantic import BaseModel


class FieldAnswer(BaseModel):
    fieldName: str
    answer: str
    confidence: float