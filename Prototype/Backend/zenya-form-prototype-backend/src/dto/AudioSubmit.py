import wave
from pydantic import BaseModel


class AudioSubmit(BaseModel):
    audioFile: wave