from pydantic import BaseModel
from typing import List

class MultipleChoiceEntity(BaseModel):
    context: str
    candidate_labels: List[str]