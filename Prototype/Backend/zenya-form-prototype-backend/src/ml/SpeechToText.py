from .ISpeechToText import ISpeechToText
import speech_recognition as sr
import os
import ffmpeg

class SpeechToText(ISpeechToText):
    def __init__(self ):
        self

    def speechToText(self, spoken_context: bytes) -> str:
        context = ''
        webm_file = './converted.webm'
        webm_path = (os.getcwd() + '/converted.webm')
        wav_file = './out.wav'
        wav_path =(os.getcwd() + '/out.wav')

        # write to webm file
        with open(webm_file, 'wb') as f:
            f.write(spoken_context)
            
        # Convert webm to wav
        ffmpeg.input(webm_file).output(wav_file, format='wav').run()
        
        r = sr.Recognizer()
        videototext = sr.AudioFile(wav_path)
        with videototext as source:
            audio = r.record(source)
        
        try:
            context = r.recognize_google(audio)
            print("Transcription: " + context)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        
        # removing recordings
        os.remove(webm_path)
        os.remove(wav_path)
        return context