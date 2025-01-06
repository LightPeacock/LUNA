import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import wikipedia
import pywhatkit
import csvreader

#Setting up engine 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)



#Speak function this makes the AI speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#atkes what we say as input
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 2
        audio = r.listen(source,timeout=5,phrase_time_limit=5)

        try:
            query = r.recognize_google(audio,language="en-in")
            speak(query)
        
        except Exception as e:
            speak("Sorry say that again please..")
            return None
        return query

#Used to greet you according to time
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning, Sir!")
    elif hour >= 13 and hour <=18:
        speak("Good afternoon, Sir!")
    
    else:
        speak("Good evening, Sir!")
    
def waking():
    speak("Always at your service, Sir!!")

def intro():
    speak("Hello!. I am SAGE (Smart Assistance for Guidence and efficiency). A Desktop assistant for C L Narayanan. My primary task is to help him complete his tasks easily and in a more efficent way")




