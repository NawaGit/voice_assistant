from operator import truediv
import warnings
import pyttsx3
import speech_recognition as sr
import pyaudio
from gtts import gTTS
import playsound
import os
import datetime
import calendar
import random
import wikipedia
import webbrowser
import shutil
import requests
import winshell
import pyjokes
import ctypes
import subprocess
from playsound import playsound
warnings.filterwarnings("ignore")
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("How may I help you")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        playsound("./water_droplet.mp3")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Not Understand....")
        return "None"
    return query
def name():
    speak("What should I call you sir!")
    name = takeCommand()
    speak("Welcome ")
    speak(name)
    columns = shutil.get_terminal_size().columns
    print("Welcome Mr.", name.center(columns))
if __name__ == "__main__":
    wishMe()
    name()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia,""")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            speak(results)
        elif'open youtube'in query:
            webbrowser.open("youtube.com")


        elif "weather" in query:
             
            # Google Open weather website
            # to get API of Open weather
                api_key = "Api key"
                base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
                speak(" City name ")
                print("City name : ")
                city_name = takeCommand()
                complete_url = base_url + "appid =" + api_key + "&q =" + city_name
                response = requests.get(complete_url)
                x = response.json()
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")




