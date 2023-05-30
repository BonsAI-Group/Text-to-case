import wave
from .ISpeechToText import ISpeechToText
import speech_recognition as sr
import soundfile
import os

class SpeechToText(ISpeechToText):
    def __init__(self ):
        self

    def speechToText(self, spoken_context: wave) -> str:
        context = ''
        converted_audio_path = 'converted.wav'
        audio_path = os.getcwd() + '//audio_files//' + converted_audio_path
        print(audio_path)
        
        data, samplerate = soundfile.read(spoken_context)
        soundfile.write(converted_audio_path, data, samplerate, subtype='PCM_16')
        
        
        r = sr.Recognizer()
        with sr.WavFile(audio_path) as source:              # use "test.wav" as the audio source
            audio = r.record(source)                        # extract audio data from the file

        try:                  
            print("Transcription: " + r.recognize_google(audio))   # recognize speech using Google Speech Recognition
            context = r.recognize_google(audio)                  
        except LookupError:                                        # speech is unintelligible
            print("Could not understand audio")
            
        return context