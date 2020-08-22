import pyttsx3
import os
import datetime
hour=datetime.datetime.now().hour
if hour>=0 and hour<12:
        pyttsx3.speak("Hello,Good Morning")
elif hour>=12 and hour<16:
        pyttsx3.speak("Hello,Good Afternoon")
elif hour>=16 and hour<20:
        pyttsx3.speak("Hello,Good Evening")
else :
        pyttsx3.speak("Hello,Good night")
pyttsx3.speak("please sir enter your good name so we can start conversation with each other ")
print("\033[1;36;47m enter your name: ",end="")
u=input()
pyttsx3.speak("welcome")
pyttsx3.speak(u)
engine = pyttsx3.init()
while True:
    print("tell me sir what can i do for you next:",end="")
    pyttsx3.speak("tell me sir what can i do for you next")
    p=input()
    if ("what can you do"in p):
        engine.setProperty('rate', 150)
        pyttsx3.speak("I am your personal, virtual assistant ,I can do simple tasks like open a program for you,open a website for you,shutdown your computer,clean your screen ,can tell which files are stored in your current folder,predict time and tell top headlines for times of india newspaper and much more ")
        pyttsx3.speak("so let's start what task i can perform for you first ,If you get bored simply text exit or quit")
    elif(("open"in p) or ("launch" in p )or("start"in p) or"run" in p or "execute"in p)and("chrome"in p or "web browser"in p or "browser"in p):
        pyttsx3.speak("loading sir.....")
        print("loading sir....")
        os.system(" start chrome")
    elif("exit"in p or"quit"in p or"turn-off"in p or "close" in p):
        pyttsx3.speak("thank you have a nice day")
        break
    elif(("clear"in p) or ("screen"in p or "console"in p)):
        os.system("cls")
    elif(("open"in p) or ("launch" in p )or("start"in p) or"run" in p or "execute"in p)and("notepad"in p or "text editor"in p):
        pyttsx3.speak("loading sir.....")
        print("loading sir....")
        os.system("notepad")
    elif(("open"in p) or ("launch" in p )or("start"in p) or"run" in p or "execute"in p)and("ms paint"in p or "paint"in p):
        pyttsx3.speak("loading sir.....")
        print("loading sir....")
        os.system("mspaint.exe")
    elif(("open"in p) or ("start"in p)  or ("execute"in p) or "run"in p)and("youtube"in p ):
        pyttsx3.speak("loading sir.....")
        print("loading sir....")
        os.system(" start chrome https://www.youtube.com/ ")
    elif(("open"in p) or ("start"in p)  or ("execute"in p))and("media"in p or "player"in p  ):
        os.system("wmplayer")
        pyttsx3.speak("loading sir.....")
        print("loading sir....")
    elif("today's headlines"in p or "news"in p):
        pyttsx3.speak("loading sir.....")
        print("loading sir....")
        os.system("start chrome https://timesofindia.indiatimes.com/home/headlines")
    elif(("open"in p) or  ("read"in p))and("folder" in p  ):
        os.system("dir")   #show all files in current folder
    elif(("open"in p) or  ("tell"in p) or "today"in p)and("weather"in p or"report" in p  ):
        pyttsx3.speak("loading sir.....")
        print("loading sir....")
        os.system("start chrome weather.com ")
    elif("tell"in p or "show"in p or "today"in p)and ("date"in p):
        os.system("date")
    elif("tell"in p or "show"in p or "present"in p)and ("time"in p):
        os.system("time")
    elif("open"in p or "show"in p)and("file"in p or "docx"in p):
        t=input("enter the file name you want to open::")
        i=os.system("start t")
        if i==1:
            engine.setProperty('rate', 150)
            pyttsx3.speak("file not found  sir please type file name correctly")
        elif i==0:
            pyttsx3.speak("done sir")
    elif("show"in p or "open"in p) and ("calculator"in p or"calc"in p):
        pyttsx3.speak("loading sir.....")
        print("loading sir....")
        os.system("calc")
    elif("play"in p or"start" in p or "open" in p)and("music"in p or "song" in p):
        pyttsx3.speak("loading sir.....")
        print("loading sir....")
        os.system("start chrome https://music.youtube.com/browse/FEmusic_language_selection")
    elif("shutdown " in p or "turn off " in p) and("computer"in p or "windows"in p):
        pyttsx3.speak("I am closing your computer please save your work")
        os.system("shutdown /s ")
    else:
        engine.setProperty('rate', 150)
        pyttsx3.speak("this feature is not available in me, may be available in future updates")
        print("this feature is not available in me it may be available in future updates")
