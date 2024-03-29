from pydantic import BaseModel


class FieldAnswer(BaseModel):
    fieldName: str
    answer: list[str]
    confidence: list[float]
    isTrusted: list[bool]
