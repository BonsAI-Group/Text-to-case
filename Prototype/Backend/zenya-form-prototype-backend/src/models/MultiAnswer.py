from pydantic import BaseModel


class MultiAnswer(BaseModel):
    answers: list[str]
    confidence: list[float]
    isTrusted: list[bool]
    