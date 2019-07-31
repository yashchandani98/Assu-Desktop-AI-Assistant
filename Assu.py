import pyttsx3
import speech_recognition as speech
import wikipedia
import datetime
import os
import webbrowser
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
wishes=['good morning','good evening','good afternoon']
websites = {'youtube': 'youtube.com','facebook':'facebook.com','google':'google.com','gmail':'gmail.com'}
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def initial():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Buddy!")
        print("Assu:Good Morning Buddy!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Buddy!")
        print("Assu:Good Afternoon Buddy!")
    else:
        speak("Good Evening Buddy!")
        print("Assu:Good Evening Buddy!")
def listen():
    r = speech.Recognizer()
    with speech.Microphone() as src:
        print("Listening...")
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
        try:
            string = listen().lower()
            if string in wishes:
                initial()
            elif "what is your name" in string:
                speak("My name is Assu.")
                print("Assu:My name is Assu.")
            elif "wikipedia" in string:
                speak("Collecting information from Wikipedia")
                summ=wikipedia.summary("New York")
                speak("According to Wiipedia:")
                print(summ)
                speak(summ)
            elif "open" in string:
                for key in websites:
                    if key in string:
                        webbrowser.open(websites[key])
            elif "time" in string:
                time=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {time}")
                print(f"Assu:The time is {time}")
            elif "date" in string:
                date=datetime.datetime.now().strftime("%d:%B%Y")
                speak(f"The date is {date}")
                print(f"Assu:The date is {date}")
            elif "today" in string:
                day = datetime.datetime.now().strftime("%A")
                speak(f"Today is {day}")
                print(f"Assu:Today is {day}")
        except Exception as e:
            print(e)