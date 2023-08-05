import keyboard
import pydirectinput
import pyttsx3
import pyaudio
import speech_recognition as sr
import random
from requests import get
import pywhatkit
import smtplib
import cv2
import winsound
import pyfirmata
import datetime
import wikipedia
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import math
import webbrowser
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
from tkinter import *
from PIL import ImageTk, Image
import pyjokes
from pyjokes import get_joke
from email.message import EmailMessage
import pyautogui as pg
import time
import mysql.connector
from datetime import timedelta
from datetime import date
import time

# J.A.R.V.I.S. starts here

def start_of_jarvis():
    import OTP_sender

    pydirectinput.click(x=710, y=618)

    o = OTP_sender.otp()
    user_name = o[0]
    name = o[1]
    email = o[2]
    password = o[3]
    gender = o[4]

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[0].id)
    # print(voices[0].id)
    engine.setProperty("rate", 180)
    engine.setProperty('volume', 1)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def take_command():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("LISTENING BOSS.....")
            # r.pause_threshold = 2
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            audio = r.listen(source)
            try:
                query = r.recognize_google(audio, language='en-in')
                print("boss said : ", query)
            except Exception as e:
                return "none"
            return query


    def wishme():
        if gender == 'Male' or gender == 'M':
            speak("hello mister" + name)
        else:
            speak("hello mrs" + name)

        hour = int(datetime.datetime.now().hour)
        if (hour >= 0) and (hour < 12):
            speak("good morning boss")
            strTime = datetime.datetime.now().strftime("%I %M %p")
            speak("The time now is")
            speak(strTime)
            print("The time is", strTime)
            y = int(datetime.datetime.now().year)
            m = int(datetime.datetime.now().month)
            d = int(datetime.datetime.now().day)
            a = ["s", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
            b = a[m]
            speak(f" boss the date is {d} {b} {y} ")
            print("The current date is", d, b, y)
            day = datetime.datetime.now().strftime("%A")
            speak(f"boss today's day is{day}")
            print(f"Boss today's day is {day}")

        elif (hour >= 12) and (hour < 18):
            speak("good afternoon boss")
            strTime = datetime.datetime.now().strftime("%I %M %p")
            speak("The time now is")
            speak(strTime)
            print("The time is", strTime)
            y = int(datetime.datetime.now().year)
            m = int(datetime.datetime.now().month)
            d = int(datetime.datetime.now().day)
            a = ["s", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
            b = a[m]
            speak(f" boss the date is {d} {b} {y} ")
            print("The current date is", d, b, y)
            day = datetime.datetime.now().strftime("%A")
            speak(f"boss today's day is{day}")
            print(f"Boss today's day is {day}")

        else:
            speak("good evening boss")
            s = datetime.datetime.now().strftime("%I %M %p")
            speak("The time now is")
            speak(s)
            print("The time is", s)
            y = int(datetime.datetime.now().year)
            m = int(datetime.datetime.now().month)
            d = int(datetime.datetime.now().day)
            a = ["s", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
            b = a[m]
            speak(f" boss the date is {d} {b} {y} ")
            print("The current date is", d, b, y)
            day = datetime.datetime.now().strftime("%A")
            speak(f"boss today's day is{day}")
            print(f"Boss today's day is {day}")

        speak("i am Jarvis")
        speak("i am online and ready")

        import birthdays
        birthdays.birthday()

    def jarvis():
        wishme()
        time.sleep(1)
        speak("PRESS 'T' FOR TYPED COMMANDS AND 'S' FOR SPOKEN COMMANDS")
        print("PRESS 'T' FOR TYPED COMMANDS AND 'S' FOR SPOKEN COMMANDS")
        ch = input("BOSS DO YOU WANT TO GIVE ME SPOKEN COMMANDS\nOR TYPED COMMANDS : ").upper()
        ch = ch.strip()
        if ch == 'T' or ch == 'TEXT' or ch == 'TYPE':
            while True:
                q = input("Enter your command : ").lower()
                q = q.strip()
                import typed_placement
                typed_placement.placement(q)


        elif ch == "S" or ch == "SPEECH" or ch == "SPOKEN":
            while True:
                q = take_command().lower()
                q = q.strip()
                import typed_placement
                typed_placement.placement(q)

    jarvis()


