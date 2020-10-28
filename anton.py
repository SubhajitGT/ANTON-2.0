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
engine = pyttsx3.init()


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


