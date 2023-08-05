import time
import pyttsx3
import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pyautogui as pg
import pyaudio
import speech_recognition as sr

def distance_search():
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

    speak("Boss enter the first destination you want to search for?")
    choice = take_command().lower()
    speak("Boss enter the second destination you want to search for?")
    choice1 = take_command().lower()
    speak("Gotcha boss")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s = Service("C:\\webdrivers\\chromedriver.exe")
    browser = webdriver.Chrome(service=s, options=options)
    browser.maximize_window()
    browser.get("https://www.google.com/maps")
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="minimap"]/div/div[2]/button').click()
    time.sleep(1)

    if choice == "home":
        search = browser.find_element(By.NAME, "q")
        search.send_keys("23.700016, 86.954183")

    else:
        search = browser.find_element(By.NAME, "q")
        search.send_keys(choice)

    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="searchbox-searchbutton"]').click()
    time.sleep(3)
    browser.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="omnibox-directions"]/div/div[3]/div[2]/button').click()
    time.sleep(1)

    if choice1 == "home2":
        search1 = browser.find_element(By.XPATH, '//*[@id="sb_ifc52"]/input')
        search1.send_keys("22.790749, 87.976282")

    else:
        search1 = browser.find_element(By.XPATH, '//*[@id="sb_ifc52"]/input')
        search1.send_keys(choice1)

    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="directions-searchbox-1"]/button[1]').click()
    time.sleep(3)
    browser.find_element(By.XPATH, '//*[@id="section-directions-trip-0"]/div[1]/div[1]').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/button').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="modal-dialog"]/div/div[2]/div/div[3]/div/div/div[1]/div[4]/div[2]/div[1]/button').click()
    time.sleep(1)

    webbrowser.open("https://web.whatsapp.com/")
    time.sleep(10)
    # search button
    pg.click(x=299, y=220)
    pg.typewrite("papa voda")
    time.sleep(3)
    # name/number search
    pg.click(x=354, y=395)
    # type message
    pg.hotkey("ctrl", "v")
    time.sleep(2)
    # sending the message
    pg.click(x=1842, y=965)
    time.sleep(2)
    # minimizing the window
    time.sleep(2)
    pg.click(x=1760, y=17)
    time.sleep(1.5)
    pg.click(x=1893, y=11)
