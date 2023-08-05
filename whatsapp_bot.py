import pywhatkit
import pyautogui as pg
import webbrowser
import time
import pyttsx3
import whatsapp_group_msg_sender

def whatsapp_message():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[0].id)
    # print(voices[0].id)
    engine.setProperty("rate", 180)
    engine.setProperty('volume', 1)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    speak("DO YOU WANT TO SEND MESSAGE IN GROUP OR TO INDIVIDUAL PERSON")
    ch = input("DO YOU WANT TO SEND MESSAGE IN GROUP(y) OR TO INDIVIDUAL PERSON(n) (y/n) : ")

    if ch == 'n' or ch == 'no':
        print("BOSS DO YOU KNOW THE NUMBER OF THAT PERSON OR NAME OF THAT PERSON")
        inp = input("PRESS 'y' FOR NUMBER AND 'n' FOR MANE").lower()
        inp = inp.strip()
        if inp == "y" or inp == "yes":
            num = input("ENTER THE NUMBER YOU WANT TO SEND WHATSAPP MESSAGE TO : \n")
            msg = input("ENTER THE MESSAGE YOU WANT TO SEND : \n")
            while True:
                if "+91" in num:
                    pywhatkit.sendwhatmsg_instantly(num, msg, 15)
                else:
                    pywhatkit.sendwhatmsg_instantly("+91" + num, msg, 15)

                ch1 = input("DO YOU WANT TO SEND MORE (y/n) : \n")
                if ch1 == "n":
                    break

        else:
            name = input("ENTER THE PERSON'S NAME TO BE SENT ")
            message = input("ENTER THE MESSAGE TO BE SENT ")

            # TIME FORMAT

            t = input("ENTER THE TIME FORMAT ")
            if t == "H" or t == "h" or "hours" in t:
                t1 = int(input("ENTER THE TIME FORMAT IN HOURS "))
                time_format = t1 * 3600
            elif t == "M" or t == "m" or "minutes" in t:
                t1 = int(input("ENTER THE TIME FORMAT IN MINUTES "))
                time_format = t1 * 60
            elif t == "S" or t == "s" or "seconds" in t:
                t1 = int(input("ENTER THE TIME FORMAT IN SECONDS "))
                time_format = t1
            else:
                print("ERROR:PLEASE ENTER THE TIME FORMAT")

            webbrowser.open("https://web.whatsapp.com/")

            time.sleep(20)
            # print(pg.position())

            # search button
            pg.click(x=299, y=220)
            pg.typewrite(name)
            time.sleep(5)

            # name/number search
            pg.click(x=354, y=395)
            time.sleep(time_format)

            # type message
            pg.typewrite(message)
            time.sleep(2)

            # sending the message
            pg.click(x=1842, y=965)
            time.sleep(2)

            # minimizing the window
            time.sleep(5)
            pg.click(x=1760, y=17)

            pg.click(x=963, y=749)

            while True:

                a = input("DO YOU WANT TO ENTER MORE ").lower()
                if a == "yes" or a == "y" or a == "":

                    name = input("ENTER THE PERSON'S NAME TO BE SENT ")
                    message = input("ENTER THE MESSAGE TO BE SENT ")

                    # TIME FORMAT

                    t = input("ENTER THE TIME FORMAT ")
                    if t == "H" or t == "h" or "hours" in t:
                        t1 = int(input("ENTER THE TIME FORMAT IN HOURS "))
                        time_format = t1 * 3600
                    elif t == "M" or t == "m" or "minutes" in t:
                        t1 = int(input("ENTER THE TIME FORMAT IN MINUTES "))
                        time_format = t1 * 60
                    elif t == "S" or t == "s" or "seconds" in t:
                        t1 = int(input("ENTER THE TIME FORMAT IN SECONDS "))
                        time_format = t1
                    else:
                        print("ERROR PLEASE ENTER THE TIME FORMAT")

                    time.sleep(8)
                    pg.click(x=516, y=1046)

                    # search button
                    pg.click(x=299, y=220)
                    pg.typewrite(name)
                    time.sleep(5)

                    # name/number search
                    pg.click(x=354, y=395)
                    time.sleep(time_format)

                    # type message
                    pg.typewrite(message)
                    time.sleep(2)

                    # sending the message
                    pg.click(x=1784, y=967)
                    time.sleep(2)

                    # minimizing the window
                    time.sleep(5)
                    pg.click(x=1760, y=17)

                    pg.click(x=963, y=749)

                else:
                    print("OK NO PROBLEM SIR")
                    break

    else:
        whatsapp_group_msg_sender.whatsapp_group()
