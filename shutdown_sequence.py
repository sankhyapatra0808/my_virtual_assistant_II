import os
import pydirectinput as pd
import pyttsx3

def shutdown():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[0].id)
    # print(voices[0].id)
    engine.setProperty("rate", 180)
    engine.setProperty('volume', 1)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    speak("Alright boss shutdown sequence activated")
    os.system("shutdown /s /t 2")
    pd.click(x=1893, y=11)
