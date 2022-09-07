import speech_recognition as sr
#if i want to be able to search google...
import webbrowser
import time
import pyttsx3

from time import ctime

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def record_audio(ask = False):
    if ask:
        flywaterz_speak(ask)
    with sr.Microphone() as source:
        audio = listener.listen(source)
        voice_data = ''
        try:
            voice_data = listener.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            flywaterz_speak("i can't understand")
        except sr.RequestError:
            flywaterz_speak('sorry my service is down')
        return voice_data
def flywaterz_speak():

def respond(voice_data):
        if 'what is your name' in voice_data:
            flywaterz_speak('My name is flywaterz')
        if "what time is it" in voice_data:
            flywaterz_speak(ctime())
        if "search" in voice_data:
            search = record_audio('what do you want to search for?')
            url= 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            flywaterz_speak('Here is what i found' + '' + search)
#we need it to know what we are saying
#I created a variable search into record audio so that it wont
# print but listen and search in web
        if "find location" in voice_data:
            location = record_audio('what is the location?')
            url= 'https://google.com/maps/place/' + location + '/&amp:'
            webbrowser.get().open(url)
            flywaterz_speak('Here is the location' + location)
        if 'Hello' in voice_data:
            flywaterz_speak("greetings")
        if "Thank you" in voice_data:
            flywaterz_speak("you're welcome")
        if 'exit' in voice_data:
            exit()
time.sleep(1)
flywaterz_speak('listening...')
while 1:
    voice_data = record_audio()
    respond(voice_data)
