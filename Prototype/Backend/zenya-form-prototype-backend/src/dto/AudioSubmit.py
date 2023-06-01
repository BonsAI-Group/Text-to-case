from pydantic import BaseModel

from src.models.FormItem import FormItem


class AudioSubmit(BaseModel):
    audioFile: bytes
    field: FormItem
    formName: str 