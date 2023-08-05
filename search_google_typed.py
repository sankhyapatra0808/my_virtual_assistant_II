from selenium.webdriver.chrome.service import Service
import keyboard
import pyttsx3
from selenium import webdriver
from selenium.webdriver.common.by import By

def google_search():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[0].id)
    # print(voices[0].id)
    engine.setProperty("rate", 180)
    engine.setProperty('volume', 1)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    speak("Boss what do you want to search for?")
    choice = input("BOSS, WHAT DO YOU WANT TO SEARCH : ")
    speak("Gotcha boss")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s = Service("C:\\webdrivers\\chromedriver.exe")
    browser = webdriver.Chrome(service=s, options=options)
    browser.maximize_window()
    browser.get("https://www.google.com/")
    search = browser.find_element(By.NAME, "q")
    search.send_keys(choice)
    keyboard.press_and_release("Enter")
