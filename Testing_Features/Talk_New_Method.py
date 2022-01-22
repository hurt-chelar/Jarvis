import sys
from pyttsx3 import engine, speak
from pywhatkit.misc import web_screenshot
import speech_recognition as sr # this is to take the speech 
import pyttsx3 #this is the speech to text engine 
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser as web  # this is to make searches in youtube and things like that
import os # this is to play songs and things like that 
import subprocess
import pywhatkit
from pywikihow import WikiHow , search_wikihow

engine = pyttsx3.init() # this is the inbuild voice
engine.setProperty('rate' , 200) 



def talk(text) : # this is the speak function
    engine.say(text)
    engine.runAndWait()




def take_command() : # this takes the mic 


    try : 
        listener = sr.Recognizer()
        with sr.Microphone() as source : 
            
            print('Listening .. ' )
            # listener.pause_threshold = 1  # this is to improve the time before the program things that the code is done

            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='en-in')
            command = command.lower()
            print('\n')
            print(command)
            speak(command)
    except Exception as e : # this is like storing the exception in this block
        # pass 
        print('Please say that again') 
        return "none"
        

    return command  


take_command ()