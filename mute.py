import subprocess
import keyboard
import pyttsx3
import time

def muted():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[0].id)
    # print(voices[0].id)
    engine.setProperty("rate", 180)
    engine.setProperty('volume', 1)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    p = subprocess.Popen(['C:\Windows\System32\mblctr.exe'])
    time.sleep(0.1)
    keyboard.press_and_release('m')
    time.sleep(0.1)
    p.kill()
    speak("done boss")
    print("Ok done!")
