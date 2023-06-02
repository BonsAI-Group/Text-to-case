import io
import wave
from .ISpeechToText import ISpeechToText
import speech_recognition as sr
import soundfile
import os

class SpeechToText(ISpeechToText):
    def __init__(self ):
        self

    def speechToText(self, spoken_context: bytes) -> str:
        context = ''
        converted_audio_path = 'converted.wav'
        audio_dir = os.path.dirname(os.path.abspath(__file__))
        # go up one directory
        audio_dir = os.path.dirname(audio_dir)
        audio_path = os.path.join(audio_dir, 'audio_files', converted_audio_path)
        
        # Write the spoken context to a WAV file
        with open(audio_path, 'wb') as f:
            f.write(spoken_context)
        
        # Load the WAV file and transcribe the audio
        data, samplerate = soundfile.read(audio_path)
        r = sr.Recognizer()
        with sr.AudioFile(audio_path) as source:
            audio = r.record(source)
        
        try:
            context = r.recognize_google(audio)
            print("Transcription: " + context)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        
        return context