import pyttsx3
import datetime
from time import ctime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

                               

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good morning sir ')
    elif hour>=12 and hour<18:
        speak('Good afternoon sir')
    elif hour>=18 and hour<24:
        speak('Good evening sir')
    speak('What can I do for you')
    
    
    

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Alexa : listening...' ,end='\n')
        r.pause_threshold=0.5
        audio=r.listen(source)
        
    try:
        print('Alexa : Recognizing...')
        query=r.recognize_google(audio,language='en-in')
        print("you said : {}\n".format(query))
    except Exception as e:
        # print(e)
        speak("didn't get you ,  try again")
        print(end='\n')
        
        return "None"
    return query



if __name__ == '__main__':
    wishme()
    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia')
            query=query.replace('wikipedia',"")
            results=wikipedia.summary(query,sentences=2)
            speak('according to wikipedia')
            speak(results)
            print(results)

        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com/search?client=opera&q=&sourceid=opera&ie=UTF-8&oe=UTF-8')
            speak('opening youtube')
            if 'turn off' in query:
                speak('turning off')
                break
            
        elif 'open google' in query:
            webbrowser.open('https://www.google.com/search?client=opera&q=&sourceid=opera&ie=UTF-8&oe=UTF-8')
            speak('opening google search')
            if 'turn off' in query:
                speak('turning off')
                break
        
        elif 'open stack overflow' in query:
            webbrowser.open('https://www.stackoverflow.com/search?client=opera&q=&sourceid=opera&ie=UTF-8&oe=UTF-8')
            speak('opening stack overflow ')
            if 'turn off' in query:
                speak('turning off')
                break

        elif 'play music' in query:
            music_dir = "E:\\Songs"
            songs=os.listdir(music_dir)
            
            
            # random number---->
            
            for i in songs:
                r= random.randint(0,6)
            song=''.join(songs[r])
            songname=song.rstrip('.mp3')
            os.startfile(os.path.join(music_dir,songs[r]))
            speak('now playing')
            speak(songname)
            if 'turn off' in query:
                speak('turning off')
                break
                  

        elif 'the time' in query:
            # strTime=datetime.datetime.now().strftime("%H:%m")       
            speak('the time is')
            speak(ctime())

        elif 'turn off'  in query:
            speak('turning off, sir ') 
            break

        
        elif 'who created you' in query:
            speak("Mr. Divyansh Rajak has created me.")

        elif 'tell me about your creator'  in query:
            speak('My creator is a python developer who has currently graduated bachelors in engineering')
        
        
        elif 'search on youtube ' in query:
            search=query.lstrip('search on youtube ')
            
            webbrowser.open('https://www.youtube.com/results?search_query={}'.format(search))

        elif 'search ' in query:
            search_list=query.split()
            x=search_list.pop(0)
            str_search=' '.join(search_list)
            speak('showing results for ')
            speak(str_search)
    
            webbrowser.open('https://www.google.com/search?client=opera&q={}&sourceid=opera&ie=UTF-8&oe=UTF-8'.format(str_search))

        elif 'shutdown' in query:
            speak('are you sure')
            choice=takeCommand().lower()
            if 'yes' in choice:
                os.system("shutdown /s /t 1")
            
        elif 'close ' in query:
            c_list=query.split()
            print(c_list)
            x=c_list.pop[0]
            close_obj=c_list[0]
            os.system("TASKKILL /F /IM {}.exe".format(close_obj))
            speak('killed {}'.format(close_obj))
            

        elif 'close code and shutdown' in query:
            speak('closing vs code and shutting down')
            os.system("TASKKILL /F /IM code.exe")
            os.system("shutdown /s /t 1")

        

