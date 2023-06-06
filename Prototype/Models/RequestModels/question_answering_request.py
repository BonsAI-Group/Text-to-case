from pydantic import BaseModel
from Entities.question_answering_entity import QuestionAnsweringEntity

class QuestionAnsweringRequest(BaseModel):
    model: str
    payload: QuestionAnsweringEntity