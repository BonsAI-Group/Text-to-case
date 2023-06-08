from pydantic import BaseModel

class QuestionAnsweringEntity(BaseModel):
    context: str
    question: str
