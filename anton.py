import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import psutil
import pyjokes
import os
import pyautogui
import random
import json
import requests
from urllib.request import urlopen
import wolframalpha

engine = pyttsx3.init()
wolframalpha_app_id = '7XH6XL-V33A2EEW9G'


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is:")
    speak(Time)

def date_():
    year=datetime.datetime.now().year
    month=datetime.datetime.now().month
    date=datetime.datetime.now().day
    speak("The current date is:")
    speak(year)
    speak(month)
    speak(date)

def wishme():
    speak("Welcome Back Subhajit!")
    time_()
    date_()
    #Greetings
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("Good morning Subhajit")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Subhajit")
    elif hour>=18 and hour<=24:
        speak("Good evening Subhajit")
    else:
        speak("Good Night Subhajit")
    speak("Anton 2.0 is ready for work. Let's start.")

def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-US')
        print(query)
    except Exception as e:
        print(e)
        print("Say it again!")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()

    server.login('subhajitguha79@gmail.com','Gmail@2019')
    server.sendmail('subhajitguha79@gmail.com',to,content)
    server.close()

def cpu():
    usage=str(psutil.cpu_percent())
    speak("CPU is at"+usage)

    battery=psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def joke():
    speak(pyjokes.get_joke())

def screenshot():
    img=pyautogui.screenshot()
    img.save('C:/Users/SUBHAJIT/Pictures/Screenshots/ss.png')

if __name__ == "__main__":


    wishme()

    while True:
        query = TakeCommand().lower()

        if 'time' in query:  #tell the time
            time_()

        elif 'date' in query:
            date_()

        elif 'wikipedia' in query:
            speak("Searching...")
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=3)
            speak('According to Wikipedia')
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content=TakeCommand()
                speak("Who is the receiver")
                receiver=input("Enter receiver's email:")
                to=receiver
                sendEmail(to,content)
                speak(content)
                speak('Email sent')

            except Exception as e:
                print(e)
                speak("Unable to send...")

        elif 'search in chrome' in query:
            speak("What to search?")
            chromepath='C:/Users/SUBHAJIT/AppData/Local/Google/Chrome/Application/chrome.exe %s'

            search=TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'search youtube' in query:
            speak("What to search?")
            search_Term=TakeCommand().lower()
            speak("Here we go to youtube!")
            wb.open('https://www.youtube.com/results?search_query='+search_Term)

        elif 'search google' in query:
            speak("What to search?")
            search_Term = TakeCommand().lower()
            speak("Searching....")
            wb.open('https://www.google.com/search?q='+search_Term)

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            joke()

        elif 'go offline' in query:
            speak("Going offline Bye!")
            quit()

        elif 'word' in query:
            speak("Opening MS-word")
            ms_word=r'C:/Program Files/Microsoft Office/Office15/WINWORD.EXE'
            os.startfile(ms_word)

        elif 'excel' in query:
            speak("Opening MS-excel")
            ms_excel=r'C:/Program Files/Microsoft Office/Office15/EXCEL.EXE'
            os.startfile(ms_excel)

        elif 'power point' in query:
            speak("Opening MS-PowerPoint")
            ms_pp=r'C:/Program Files/Microsoft Office/Office15/POWERPNT.EXE'
            os.startfile(ms_pp)

        elif 'Notepad plus-plus' in query:
            speak("Opening Notepad plus-plus, coding begins.....")
            np_pp=r'C:/Program Files/Notepad++/notepad.exe'
            os.startfile(np_pp)

        elif 'Code Blocks' in query:
            speak("Opening CodeBlock, coding begins.....")
            cb=r'C:/Program Files (x86)/CodeBlocks/codeblocks.exe'
            os.startfile(cb)

        elif 'Write a note' in query:
            speak("What Should I write?")
            notes=TakeCommand()
            file=open('note.txt','w')
            speak("Include date and time?")
            ans=TakeCommand()
            if 'yes' in ans or 'sure' in ans:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(":-")
                file.write(notes)
                speak("Note is complete")
            else:
                file.write(notes)

        elif 'show notes' in query:
            speak("Showing notes")
            file=open('note.txt','r')
            print(file.read())
            speak(file.read())

        elif 'screenshot' in query:
            screenshot()

        elif 'play music' in query:
            songs_dir = 'C:/Users/SUBHAJIT/Music'
            music= os.listdir(songs_dir)
            speak('Which song to play?')
            speak('Select a number...')
            while('number' not in ans and ans!='random' and ans!='you choose'):
                speak("Say It again")
            if 'number' in ans:
                no = int(ans.replace('number', ''))
            elif 'random' or 'you choose' in ans:
                no = random.randint(1,100)
            ans = TakeCommand().lower()
            os.startfile(os.path.join(songs_dir,music[no]))

        elif 'remember that' in query:
            speak("What should I remember?")
            memory=TakeCommand()
            speak("Hey I remembered it"+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'Do you remember' in query:
            remember=open('memory.txt','r')
            speak("I don't forget"+remember.read())

        elif 'where is' in query:
            query=query.replace("where is","")
            location=query
            speak("User asked to locate"+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)

        elif 'news' in query:
            try:
                jsonObj = urlopen("http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=bd27e6d83958412fa45e39e6e3005a08")
                data = json.load(jsonObj)
                i=1

                speak("Here are top headlines!!")
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i=i+1

            except Exception as e:
                print(str(e))

        elif 'log out' in query:
            os.system("shutdown -1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")



