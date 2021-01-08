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


engine = pyttsx3.init()
newVoiceRate = 145
engine.setProperty('rate',newVoiceRate)
# Make the computer welcome depends on the time

dt = datetime.datetime.now()
if datetime.time(12) > dt.time() :
    engine.say("Good Morning sir")
    engine.runAndWait() 
elif dt.time() <= datetime.time(18): 
    engine.say("Good afternoon sir")
    engine.runAndWait()
else:
    engine.say("Good evening sir")
    engine.runAndWait()



time.sleep(1)
#Ask for commans
def my_command():
    engine.say("I am waiting for you")
    engine.runAndWait()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        command = r.recognize_google(audio)
        print(command)
    return command
    engine.say("")
	
edge_path = "C:\msedge.exe %s"

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
                engine.say("what do you want to search for sir")
                engine.runAndWait()
                PATH = "C:\Program Files (x86)\msedgedriver.exe"
                driver = webdriver.Edge(PATH)
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    a = r.listen(source)
                    search_result = r.recognize_google(a)
                driver.get("http://youtube.com")
                time.sleep(8)
                search_box = driver.find_element_by_name("search_query")
                search_box.send_keys(search_result)
                search_box.send_keys(Keys.RETURN)
            elif "wikipedia" in command:
                engine.say("What do you want to search for sir?")
                engine.runAndWait()
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    s = r.listen(source)
                    result = r.recognize_google(s)
                    wikresult = wikipedia.summary(result, sentences=3)
                    print(wikresult)
                    engine.say(wikresult)
                    engine.runAndWait()
                    engine.say("Do you want the full results sir?")
                    engine.runAndWait()
                    ans = r.listen(source)
                    answer = r.recognize_google(ans)
                    if "yes" in answer:
                        wikresult = wikipedia.summary(result)
                        print(wikresult)
                    else:
                        pass
            elif "google search" in command:
                engine.say("what do you want to search for sir?")
                engine.runAndWait()
                PATH = "C:\Program Files (x86)\msedgedriver.exe"
                driver = webdriver.Edge(PATH)
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    s = r.listen(source)
                    s_result = r.recognize_google(s)
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
            elif "delete file" in command:
                engine.say("")
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


        
