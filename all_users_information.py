import mysql.connector
import pyttsx3
import pydirectinput

def info():
    pydirectinput.click(x=710, y=618)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[0].id)
    # print(voices[0].id)
    engine.setProperty("rate", 180)
    engine.setProperty('volume', 1)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    speak("PLEASE ENTER THE ADMIN PASSWORD")
    passwd = input("PLEASE ENTER THE ADMIN PASSWORD : ")

    if passwd == "@SankhyaPatra0808@":
        con = mysql.connector.connect(host="localhost", user="root", password="spaytm17", database="virtual_assistant")
        cur = con.cursor()
        q = "select * from jarvis inner join jarvis_user_name on jarvis_user_name.email = jarvis.email"
        cur.execute(q)
        d = cur.fetchall()
        for i in d:
            name = i[0]
            email = i[1]
            password = i[2]
            gender = i[3]
            user_name = i[5]
            print("(name" + ", " + "email" + ", " + "password" + ", " + "gender" + ", " + "user_name)")
            print("(" + name + ", " + email + ", " + password + ", " + gender + ", " + user_name + ")")
    else:
        speak("YOU ARE NOT AUTHORISED AS THE ADMIN")
        print("YOU ARE NOT AUTHORISED AS THE ADMIN")
