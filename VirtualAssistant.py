import os
import speech_recognition as sr
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia


warnings.filterwarnings('ignore')

def recordAudio():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Say something!')
        audio = r.listen(source)

    data = ''
    try:
        data = r.recognize_google(audio)
        assistantResponse(data)
    except:
        print("Could not recognise")
    

def assistantResponse(text):
    print(text)
    # myobj = gTTS(text = text, lang='en', slow=False)
   #  myobj.save('assistant_response.mp3')
    # os.system('open assistant_response.mp3')

def theTime():
    time = str(datetime.datetime.now())
    print(time)

theTime()