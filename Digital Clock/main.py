from tkinter import *
from tkinter.ttk import *
import datetime
import pyttsx3
from time import strftime

root = Tk()
root.title('Clock')

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def whishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good Morning!")
    elif hour>= 12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you")



lbl = Label(root, font = ('calibri', 40, 'bold'), background = 'blue', foreground = 'white')

lbl.pack(anchor = 'center')
time()

mainloop()
