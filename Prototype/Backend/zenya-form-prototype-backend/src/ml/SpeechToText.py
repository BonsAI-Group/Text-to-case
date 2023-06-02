import io
import wave
from .ISpeechToText import ISpeechToText
import speech_recognition as sr
import soundfile
import os
import moviepy.editor as mp

class SpeechToText(ISpeechToText):
    def __init__(self ):
        self

    def speechToText(self, spoken_context: bytes) -> str:
        context = ''
        converted_audio_path = 'converted.webm'
        audio_dir = os.path.dirname(os.path.abspath(__file__))
        # go up one directory
        audio_dir = os.path.dirname(audio_dir)
        audio_path = os.path.join(audio_dir, 'audio_files', converted_audio_path)

        # write to webm file
        with open(audio_path, 'wb') as f:
            f.write(spoken_context)

        # convert webm to wav
        clip = mp.VideoFileClip(audio_path)
        clip.audio.write_audiofile(audio_path.replace('webm', 'wav'))
        
        # Load the WAV file and transcribe the audio
        data, samplerate = soundfile.read(audio_path.replace('webm', 'wav'))
        r = sr.Recognizer()
        with sr.AudioFile(audio_path.replace('webm', 'wav')) as source:
            audio = r.record(source)
        
        try:
            context = r.recognize_google(audio)
            print("Transcription: " + context)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        
        return context