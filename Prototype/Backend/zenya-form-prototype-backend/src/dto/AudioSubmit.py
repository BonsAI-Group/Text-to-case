from pydantic import BaseModel
from models.FormItem import FormItem

class AudioSubmit(BaseModel):
    audioFile: bytes
    field: FormItem
    formName: str 