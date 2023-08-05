import pyttsx3
import webbrowser


def open_google_now():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[0].id)
    # print(voices[0].id)
    engine.setProperty("rate", 180)
    engine.setProperty('volume', 1)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    webbrowser.open("https://www.google.com/")
    speak("Ok Boss done")
