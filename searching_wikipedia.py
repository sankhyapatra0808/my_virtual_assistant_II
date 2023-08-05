import pyttsx3
import pyaudio
import speech_recognition as sr
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
    query = take_command().lower() + " wikipedia"
    speak("Gotcha boss")
    query = query.replace("wikipedia", " ") # main command line
    results = wikipedia.summary(query, sentences=2)
    speak("according to wikipedia")
    speak("results")
    speak(results)
    print(results)
