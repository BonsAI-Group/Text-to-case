from pydantic import BaseModel

class Answer(BaseModel):
    answer: str
    confidence: float
    isTrusted: bool
        