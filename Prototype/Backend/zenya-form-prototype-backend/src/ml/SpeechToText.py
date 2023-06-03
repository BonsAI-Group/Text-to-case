from .ISpeechToText import ISpeechToText
import speech_recognition as sr
import soundfile
import os

class SpeechToText(ISpeechToText):
    def __init__(self ):
        self

    def speechToText(self, spoken_context: bytes) -> str:
        context = ''
        audio_file = './converted.webm'
        audio_path = (os.getcwd() + '//' + audio_file)
        audio_output_file = './out.wav'
        audio_output_path =(os.getcwd() + '//' + audio_output_file)

        # write to webm file
        with open(audio_file, 'wb') as f:
            f.write(spoken_context)
        print(audio_file)
        
        # Convert webm to wav
        command = "ffmpeg -i " + audio_file + " -c:a pcm_f32le " + audio_output_file
        os.system(command)
        
        # fix wav format
        converted_audio_path = audio_output_file
        data, samplerate = soundfile.read(audio_output_path)
        soundfile.write(converted_audio_path, data, samplerate, subtype='PCM_16')
        
        r = sr.Recognizer()
        videototext = sr.AudioFile(converted_audio_path)
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
        os.remove(audio_path)
        os.remove(converted_audio_path)
        return context