import pyttsx3
def placement(q):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[0].id)
    # print(voices[0].id)
    engine.setProperty("rate", 180)
    engine.setProperty('volume', 1)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    if "hello" in q:
        speak("hi boss i am jarvis")

    elif "handwriting bot" in q:
        import text_to_handwriting
        text_to_handwriting.handwriting()

    elif "mute" in q:
        import mute
        mute.muted()

    elif "play on youtube" in q:
        import youtube_video_runner
        youtube_video_runner.video_reader()

    elif "search youtube" in q:
        import youtube
        youtube.youtube_search_results()

    elif "play song on youtube" in q:
        import songs_youtube
        songs_youtube.auto_select()

    elif "open youtube" in q:
        import open_youtube
        open_youtube.opening_youtube_now()

    elif "open google" in q:
        import open_google
        open_google.open_google_now()

    elif "search google" in q:
        import search_google
        search_google.google_search()

    elif "search wikipedia" in q:
        import searching_wikipedia
        searching_wikipedia.search_wiki()

    elif "make an email" in q:
        import email_generator
        email_generator.email_generate()

    elif "open my browser" in q:
        import browser
        browser.create_browser()

    elif "send an email" in q:
        import email_bot
        email_bot.send_email_message()

    elif "send whatsapp message" in q:
        import whatsapp_bot
        whatsapp_bot.whatsapp_message()

    elif "take a photo" in q or "open camera" in q:
        import camera
        camera.camera()

    elif "recognise me" in q or "open recogniser" in q:
        import person_recognition
        person_recognition.register_users()

    elif "all user information" in q or "main info" in q:
        import all_users_information
        all_users_information.info()

    elif "search for places" in q:
        import map_finder
        map_finder.map_search()

    elif "search distance" in q or "search distance in maps" in q:
        import distance_search_spoken
        distance_search_spoken.distance_search()

    elif "shutdown" in q:
        import shutdown_sequence
        shutdown_sequence.shutdown()

    elif "restart" in q:
        import restart_sequence
        restart_sequence.restart()

    elif "lights" in q and "on" in q:
        import lights_on
        lights_on.lights_on()

    elif "lights" in q and "off" in q:
        import lights_off
        lights_off.lights_off()

    elif "exit" in q:
        quit()
