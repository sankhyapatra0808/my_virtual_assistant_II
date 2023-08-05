import pyfirmata
import pyttsx3

def lights_on():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[0].id)
    engine.setProperty("rate", 180)
    engine.setProperty('volume', 1)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    speak("Yes boss let me just check for any error")
    try:
        board = pyfirmata.Arduino('COM3')
        board.digital[7].mode = pyfirmata.OUTPUT
        board.digital[7].write(1)
        speak("ok boss gotcha")
        board.digital[7].write(0)

    except:
        speak("Boss there is some network issue or something else")
        speak("Cannot turn on light")