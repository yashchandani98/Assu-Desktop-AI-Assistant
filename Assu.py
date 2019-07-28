import pyttsx3
import speech_recognition as speech
import wikipedia
import datetime
import os
import pyaudio
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
wishes=['good morning','good evening','good afternoon']
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def initial():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Buddy!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Buddy!")
    else:
        speak("Good Evening Buddy!")
def listen():
    r = speech.Recognizer()
    with speech.Microphone() as src:
        print("Listening...")
        r.pause_threshold=2
        audio=r.listen(src)
    try:
        print("Recognizing...")
        string = r.recognize_google(audio,language="en-in")
        print(f"You:{string}\n")
    except Exception as e:
        print("Couldn't Recognize. Try again!")
        return "None"
    return string
if __name__ == "__main__":
    initial()
    speak("My name is Assu. How can I help you?")
    while True:
        string = listen().lower()
        if string in wishes:
            initial()