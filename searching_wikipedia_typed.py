import pyttsx3
import wikipedia

def search_wiki():
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
    query = input("BOSS, WHAT DO YOU WANT TO SEARCH : " + " wikipedia")
    speak("Gotcha boss")
    query = query.replace("wikipedia", " ") # main command line
    results = wikipedia.summary(query, sentences=2)
    speak("according to wikipedia")
    speak("results")
    speak(results)
    print(results)