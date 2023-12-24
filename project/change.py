import speech_recognition
import os

def sound():
		os.system("python3 record.py")
		r = speech_recognition.Recognizer()
		with speech_recognition.AudioFile('./output.wav') as source:
			audio = r.record(source)
			a=r.recognize_google(audio,language='zh-TW')
			print (a)
			return (a)
            
            