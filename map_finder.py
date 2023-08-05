import time
from selenium.webdriver.chrome.service import Service
import pyttsx3
from selenium import webdriver
from selenium.webdriver.common.by import By

def map_search():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[0].id)
    # print(voices[0].id)
    engine.setProperty("rate", 180)
    engine.setProperty('volume', 1)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    speak("Boss which place do you want to search for?")
    choice = input("BOSS, WHICH PLACE DO YOU WANT TO SEARCH : ")
    time.sleep(0.3)
    speak("Gotcha boss")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s = Service("C:\\webdrivers\\chromedriver.exe")
    browser = webdriver.Chrome(service=s, options=options)
    browser.maximize_window()
    browser.get("https://www.google.com/maps")
    search = browser.find_element(By.NAME, "q")
    search.send_keys(choice)
    browser.find_element(By.XPATH, '//*[@id="searchbox-searchbutton"]').click()
