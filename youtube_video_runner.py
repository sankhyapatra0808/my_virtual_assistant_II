from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyttsx3
import pyaudio
import speech_recognition as sr

def video_reader():
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

    speak("Boss what do you want to search for?")
    choice = take_command().lower()
    speak("Gotcha boss")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s = Service("C:\\webdrivers\\chromedriver.exe")
    browser = webdriver.Chrome(service=s, options=options)
    browser.maximize_window()
    browser.get("https://www.youtube.com/")
    search = browser.find_element(By.NAME, "search_query")
    search.send_keys(choice)
    browser.find_element(By.XPATH, '//*[@id="search-icon-legacy"]').click()
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="video-title"]/yt-formatted-string'))).click()
    try:
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="skip-button:5"]/span/button/span'))).click()
    except:
        print("Please press the skip button to continue")
