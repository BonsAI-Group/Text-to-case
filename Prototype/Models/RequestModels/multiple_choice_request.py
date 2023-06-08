from pydantic import BaseModel
from Entities.multiple_choice_entity import MultipleChoiceEntity

class MultipleChoiceRequest(BaseModel):
    model: str
    payload: MultipleChoiceEntity
    