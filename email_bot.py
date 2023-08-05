import smtplib
import ssl
from email.message import EmailMessage
import pyttsx3
import pyaudio
import speech_recognition as sr
import user_information


def send_email_message():

    a = user_information.register_users()

    name = a[0]
    email = a[1]
    password = a[2]
    gender = a[3]
    user_name = a[5]

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

    # Define email sender and receiver
    email_sender = email
    email_password = 'lncmvmoynubutqxf'
    speak("Boss please enter the email address you want to send to")
    email_receiver = input("Enter the email address you want to send to : ")
    email_receiver = email_receiver.strip()

    # Set the subject and body of the email
    speak("Boss please enter the subject you want to send")
    subject = take_command().lower()
    speak("Boss please enter the body's text you want to send")
    body = take_command().lower()

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
