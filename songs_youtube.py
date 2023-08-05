import time
from selenium.webdriver.chrome.service import Service
import pyttsx3
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def auto_select():
    l = []

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[0].id)
    # print(voices[0].id)
    engine.setProperty("rate", 180)
    engine.setProperty('volume', 1)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    speak("Boss have you entered any artists name previously in my database?")
    print("Boss have you entered any artists name previously in my database?")
    speak("if you want to add artists name just type append")
    print("if you want to add artists name just type append")
    ch1 = input("(y / n / append) : ").lower()
    if ch1 == "n":
        print("Alright sir you need to enter some details")

        def write_f():
            a1 = 0
            abc = open(r"D:\youtube\songs.txt", "w")
            # n = int(input("enter the number of songs"))
            # for i in range(n):
            while True:
                nm = input("Enter the artist's name you like ").lower()
                abc.write(nm + "\n")
                ch = input("Do you want to enter more(yes/no) ").lower()
                a1 += 1
                if ch == "no":
                    print("ok boss")
                    break
            abc.close()

            return a1

        def read_f():
            abc = open(r"D:\youtube\songs.txt", "r")
            str1 = " "
            while str1:
                str1 = abc.readlines()
                for i in str1:
                    a = i.replace("\n", " ")
                    l.append(a)
                return l
            abc.close()

        write_f()
        print("songs entered")
        name = read_f()
        print(name)

    elif ch1 == "y":
        def read_f():
            abc = open(r"D:\youtube\songs.txt", "r")

            ab = abc.readlines()
            for j in ab:
                a = j.replace("\n", " ")
                l.append(a)
            abc.close()

            return l

        print("songs are already entered")
        name = read_f()
        print(name)

    else:
        ap_file = open(r"D:\youtube\songs.txt", "a")
        while True:
            nm = input("Enter the artist's name you like ").lower()
            ap_file.write(nm + "\n")
            ch = input("Do you want to enter more(yes/no) ").lower()
            if ch == "no":
                print("ok boss")
                break
        ap_file.close()

    speak("ok boss give me a minute to load")

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s = Service("C:\\webdrivers\\chromedriver.exe")
    browser = webdriver.Chrome(service=s, options=options)
    browser.maximize_window()
    browser.get("https://www.youtube.com/")
    search = browser.find_element(By.NAME, "search_query")
    choice = random.choice(name)
    search.send_keys(choice)
    browser.find_element(By.XPATH, '//*[@id="search-icon-legacy"]').click()
    WebDriverWait(browser, 60).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="video-title"]/yt-formatted-string'))).click()
    try:
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="skip-button:5"]/span/button/span'))).click()
    except:
        print("Please press the skip button to continue")
