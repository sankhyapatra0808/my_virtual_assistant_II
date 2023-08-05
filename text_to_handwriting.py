def handwriting():
    import pyttsx3
    import pyaudio
    import speech_recognition as sr
    import pywhatkit

    print("PLEASE TYPE SPEAK FOR SPEAK TEXT OR TYPE FOR TYPE TEXT")
    ch = input("").upper()
    if ch == "SPEAK":
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty("voices")
        engine.setProperty('voice', voices[0].id)
        # print(voices[0].id)
        engine.setProperty("rate", 180)
        engine.setProperty('volume', 1)

        def speak(audio):
            engine.say(audio)
            engine.runAndWait()

        def takeCommand():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.pause_threshold = 2
                r.energy_threshold = 10000
                r.adjust_for_ambient_noise(source, 1.2)

                audio = r.listen(source)
                try:
                    query = r.recognize_google(audio, language='en-in')
                    print("boss said : ", query)
                except Exception as e:
                    return "none"
                return query

        query = takeCommand().capitalize()
        pywhatkit.text_to_handwriting(query, "name.png", [0, 0, 138])


    elif ch == "TYPE":
        inp = input("Enter the text").capitalize()
        pywhatkit.text_to_handwriting(inp, "name.png", [0, 0, 138])


    else:
        print("please choose between SPEAK and TYPE")
        handwriting()
