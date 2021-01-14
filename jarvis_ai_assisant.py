import pyttsx3
import os
import subprocess
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
'''from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC'''
from bs4 import BeautifulSoup
import requests
import speech_recognition as sr
#from gtts import gTTS
import datetime
import time 
import wikipedia
import send2trash
import subprocess

engine = pyttsx3.init()
newVoiceRate = 145
engine.setProperty('rate',newVoiceRate)

edge_path = "C:\msedgedriver.exe"

def speak(text):
    engine.say(text)
    engine.runAndWait()


# Make the computer welcome depends on the time

dt = datetime.datetime.now()
if datetime.time(12) > dt.time() :
    speak("Good morning sir")
elif dt.time() <= datetime.time(18): 
    speak("Good afternoon sir")
else:
    speak("Good evening sir")


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        wish = r.recognize_google(audio)
        print(wish)
    return wish
   


time.sleep(1)
#Ask for commands
def my_command():
    speak("I am waiting for you")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        command = r.recognize_google(audio)
        print(command)
    return command
    

def send_email():
    port = 465
    password = str(input("Enter your password:"))
    context = ssl.create_default_context()
    if len(request['items']>0):
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login("makjohn32@gmail.com", password)
            message = str(input("Enter the message you want to send:"))
            sender = "makjohn32@gmail.com"
            receiver = str(input("Enter the message you want to send"))
            server.sendmail(sender, receiver, message)
            print ("Email sent...")
            server.quit()


#All the commands included here
if __name__ == "__main__":

    while True:

        try:
            command = my_command().lower()
            if "open google" in command:
                 webbrowser.open("https://www.google.com")
            elif "open youtube" in command:
                 webbrowser.open("http://youtube.com")
            elif "open gmail" in command:  
                webbrowser.open("http://gmail.com")
            elif "find on youtube" in command:
                speak("What do you want to search for sir?")
                search_result = str(listen())
                driver = webdriver.Edge(edge_path)
                driver.get("http://youtube.com")
                time.sleep(8)
                search_box = driver.find_element_by_name("search_query")
                search_box.send_keys(search_result)
                search_box.send_keys(Keys.RETURN)
            elif "wikipedia" in command:
                speak("What do you want to search for sir?")
                result = str(listen())
                wikresult = wikipedia.summary(result, sentences=2)
                print(wikresult)
                speak(wikresult)
                speak("Do you want the foul results sir?")
                ans = r.listen(source)
                answer = r.recognize_google(ans)
                if "yes" in answer:
                    wikresult = wikipedia.summary(result)
                    print(wikresult)
                else:
                    pass
            elif "google search" in command:
                speak("What do you want to search for sir?")
                PATH = "C:\Program Files (x86)\msedgedriver.exe"
                driver = webdriver.Edge(edge_path)
                s_result = listen()
                driver.get("https://www.google.com")
                search = driver.find_element_by_name("q")
                search.send_keys(s_result)
                search.send_keys(Keys.RETURN)        
            elif "open edge" in command:
                subprocess.Popen("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")    
            elif "open notepad" in command:
                subprocess.Popen("notepad.exe")
            elif "take a note" in command:
                date = datetime.datetime.now()
                file_name = str(date).replace(":", "-") + "-note.txt"
                engine.say("what do you want to write sir?")
                engine.runAndWait()
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    nt = r.listen(source)
                    note = r.recognize_google(nt) 
                with open(file_name, "w") as f:
                    f.write(note)
                subprocess.Popen(["notepad.exe", file_name])       
            elif "send email" in command:
                send_email()
            elif "go to sleep" in command:
                engine.say("I'm gonna take a nap")
                engine.runAndWait()
                print("Going to sleep")#would be the command for turning off the assistant
                break
            else:
                 print("Unknown command")
        except:
            print("Exception")
            time.sleep(5)        


        
