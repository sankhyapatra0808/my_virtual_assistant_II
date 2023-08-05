import random
import pyttsx3
import pyaudio
import speech_recognition as sr

def email_generate():
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

    s = random.randint(1, 44)
    l1 = []
    speak("Boss please enter your name")
    name = take_command().lower()
    speak("Boss please enter your title")
    title = take_command().lower()
    speak("Boss please enter your date of birth")
    dob = take_command().lower()
    for i in dob:
        if i.isdigit() is True:
            l1.append(i)

    if s == 1:
        email = name + title + random.choice(l1) + random.choice(l1) + random.choice(l1) + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 2:
        email = name + "." + title + random.choice(l1) + random.choice(l1) + random.choice(l1) + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 3:
        email = name + title + "." + random.choice(l1) + random.choice(l1) + random.choice(l1) + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 4:
        email = name + title + "@gmail.com"
        print(email)

    if s == 5:
        email = name + "." + title + "@gmail.com"
        print(email)

    if s == 6:
        email = name + random.choice(l1) + random.choice(l1) + random.choice(l1) + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 7:
        email = name + "." + random.choice(l1) + random.choice(l1) + random.choice(l1) + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 8:
        email = title + random.choice(l1) + random.choice(l1) + random.choice(l1) + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 9:
        email = title + "." + random.choice(l1) + random.choice(l1) + random.choice(l1) + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 10:
        email = name + "@gmail.com"
        print(email)

    if s == 11:
        email = name[0] + title[0] + "@gmail.com"
        print(email)

    if s == 12:
        email = name[0] + title[0] + random.choice(l1) + random.choice(l1) + random.choice(l1) + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 13:
        email = name[0] + title[0] + "." + random.choice(l1) + random.choice(l1) + random.choice(l1) + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 14:
        email = name[0] + "." + title[0] + "." + random.choice(l1) + random.choice(l1) + random.choice(l1) + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 15:
        email = name + title + random.choice(l1) + random.choice(l1) + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 16:
        email = name + "." + title + random.choice(l1) + random.choice(l1) + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 17:
        email = name + title + "." + random.choice(l1) + random.choice(l1) + random.choice(l1) +  "@gmail.com"
        print(email)

    if s == 18:
        email = name + random.choice(l1) + random.choice(l1) + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 19:
        email = name + "." + random.choice(l1) + random.choice(l1) + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 20:
        email = title + random.choice(l1) + random.choice(l1) + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 21:
        email = title + "." + random.choice(l1) + random.choice(l1) + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 22:
        email = name[0] + title[0] + random.choice(l1) + random.choice(l1) + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 23:
        email = name[0] + title[0] + "." + random.choice(l1) + random.choice(l1) + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 24:
        email = name[0] + "." + title[0] + "." + random.choice(l1) + random.choice(l1) + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 25:
        email = name + title + random.choice(l1) + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 26:
        email = name + "." + title + random.choice(l1) + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 27:
        email = name + title + "." + random.choice(l1) + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 28:
        email = name + random.choice(l1) + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 29:
        email = name + "." + random.choice(l1) + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 30:
        email = title + random.choice(l1) + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 31:
        email = title + "." + random.choice(l1) + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 32:
        email = name[0] + title[0] + random.choice(l1) + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 33:
        email = name[0] + title[0] + "." + random.choice(l1) + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 34:
        email = name[0] + "." + title[0] + "." + random.choice(l1) + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 35:
        email = name + title + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 36:
        email = name + "." + title + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 37:
        email = name + title + "." + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 38:
        email = name + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 39:
        email = name + "." + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 40:
        email = title + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 41:
        email = title + "." + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 42:
        email = name[0] + title[0] + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 43:
        email = name[0] + title[0] + "." + random.choice(l1) + "@gmail.com"
        print(email)

    if s == 44:
        email = name[0] + "." + title[0] + "." + random.choice(l1) + "@gmail.com"
        print(email)
