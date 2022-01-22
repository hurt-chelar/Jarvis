from pickle import TRUE
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
from Demo import match 

engine = pyttsx3.init() # this is the inbuild voice
engine.setProperty('rate' , 200) 

from datetime import date
import calendar




# Wishing definition 
def wish() : 
        hour = int(datetime.datetime.now().hour)
        if hour > 0 and hour < 12 : 
            engine.say('Good Morning Sir ')
            engine.say('I am jarvis')
            engine.say('What can I do for you ?')
            engine.runAndWait()
            
        elif hour>12 and hour <18 : 

            engine.say('Good Afternoon sir ')
            engine.say('I am jarvis')
            engine.say('What can I do for you ?')
            engine.runAndWait( )
        else: 
            engine.say('Good Evening sir ')
            engine.say('I am jarvis')
            engine.say('What can I do for you ?')
            engine.runAndWait()



# this is to search on Youtube
def YoutubeSearch(command) :
    result = 'https://www.youtube.com/results?search_query=' + command 
    web.open(result) 
    talk('this is what i found')
    exit 







# Talk function 
def talk(text) : # this is the speak function
    engine.say(text)
    engine.runAndWait()




def take_command() : # this takes the mic 


    try : 
        listener = sr.Recognizer()
        with sr.Microphone() as source : 
            
            print('Listening .. ' )
            listener.pause_threshold = 0.5  # this is to improve the time before the program things that the code is done

            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='en-in')
            command = command.lower()
            if 'jarvis' in command: 
                command = command.replace('jarvis', '')
                print(command)
                speak('Yes Sir')
    except Exception as e : # this is like storing the exception in this block
        # pass 
        print('Please say that again') 
        return "none"

    return command  



def run_jarvis() : 
        wish()
        while True:  # this is the trick to make an infinite loop 
            command = take_command()  # we are running the command function that we wrote above 


            if 'what is the time' in command : 
                time = datetime.datetime.now().strftime('%I:%M %p') # if we put i we get 12 hour format of time 
                print(time)
                curr_date = date.today()
                day = calendar.day_name[curr_date.weekday()]

                talk( "Current time is" + time +'day is' + day ) 


            elif 'open calendar' in command : 
                    web.open('https://calendar.google.com/calendar/u/0/r')
                    

            elif "play" in command : 
                song = command.replace('play', '')

                talk('Playing' + song )
                pywhatkit.playonyt(song)
            
            elif 'open timesheet' in command :
                
                web.open('https://docs.google.com/spreadsheets/d/10YOLR_U7bG9RhUtlsJ4WtrTzRcBVl4B3EZAiob7ieDY/edit#gid=0')
                
            elif 'wikipedia' in command : 
                person = command.replace('wikipedia' , '')
                info = wikipedia.summary(person, 2 )
                print(info)
                talk(info)

            elif 'joke' in command : 
                talk(pyjokes.get_joke()) 

            elif 'search on youtube' in command : 
                command = command.replace('search on youtube','')
                YoutubeSearch(command)

            elif 'open brave browser' in command : 
                subprocess.call('brave-browser')

            elif 'open visual studio code' in command : 
                print(command)
                subprocess.call('code')
            elif 'open note taking app' in command : 
                print(command) 
                subprocess.call('notion-snap')
            elif 'open whatsapp' in command :
                web.open('https://web.whatsapp.com/')

            
            elif 'sleep now' in command : 
                talk('Going into sleep mode, Sir')
                break 

            elif 'show timetable' in command or 'show time table' in command : 
                from Features import Time_Table # usually you get an error becuase it is like database.features.somgthing
                Time_Table()
            # commnad for opening the amrita website 
            elif "open" in command and "school" in command and "excel" in command:
                web.open('https://www.office.com/launch/excel?auth=2') 
            elif "open" in command and "school" in command and "email" in command : 
                web.open('https://outlook.office.com/mail/')

            elif 'open'in command and 'school' in command and 'website' in command : 
                print(command)
                if 'main' in command : 
                    from Selenium_Chrome_Automation.Selenium_automation import login
                    login()
                else : 
                    talk('is it main website')
                    command1 = take_command()
                    if 'yes' in command1 : 
                        from Selenium_Chrome_Automation.Selenium_automation import login
                        login()
                    else: 
                        exit 
            
            elif 'open slack' in command : 
                subprocess.call('slack')
                talk('opening slack')
            elif 'open typing website' in command : 
                web.open('https://monkeytype.com/')
               

            else  : 
                print('tell the command again ')



# this is the main code // the ones above are part of the functions
while True : 
    permission  = take_command()
    if 'wake up' in permission : 
        run_jarvis()
    elif 'shutdownnow' in permission or 'shutdown now' in permission  : 
        talk('Shutting down')
        sys.exit()


