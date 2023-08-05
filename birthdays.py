from tkinter import *
import pyttsx3
import random
import datetime
import os

def birthday():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[0].id)
    # print(voices[0].id)
    engine.setProperty("rate", 180)
    engine.setProperty('volume', 1)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    y = int(datetime.datetime.now().year)
    m = int(datetime.datetime.now().month)
    d = int(datetime.datetime.now().day)
    a = ["s", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    b = a[m]

    if d == 2:
        if b == "January":
            speak("sir today is your mother's birthday")

    if d == 11:
        if b == "January":
            speak("sir today is your father's birthday")

    if d == 21:
        if b == "October":
            speak("sir today is the birthday of matriya dasgupta")

    if d == 19:
        if b == "January":
            speak("sir today is the birthday of shivam mallick")

    if d == 30:
        if b == "July":
            speak("sir today is the birthday of swati")

    if d == 8:
        if b == "August":
            speak("happy birthday sir many many returns of the day")
            print("HAPPY BIRTHDAY SIR MANY MANY RETURNS OF THE DAY")
            speak("sir i have a surprise for you")
            sh = input("sir should i show it to you")
            if sh == "yes" or sh == "ok" or sh == "really":

                speak("alright sir ready for your surprise")

                music_dir = "D:\\n1"
                songs = os.listdir(music_dir)
                rn = random.choice(songs)
                os.startfile(os.path.join(music_dir, rn))

                root = Tk()
                root.title("HAPPY BIRTHDAY SIR")
                root.geometry('1280x720')
                compText = StringVar()
                userText = StringVar()
                userText.set("HAPPY BIRTHDAY MR. SANKHYA")
                userFrame = LabelFrame(root, text='STARTUPS', font=("Black ops one", 15, 'bold'))
                userFrame.pack(fill='both', expand='yes')
                left = Message(userFrame, textvariable=userText, bg="black", fg="white")
                left.config(font=('Century Gothic', 20, 'bold'))
                left.pack(fill='both', expand='yes')
                compFrame = LabelFrame(root, text='🍕🍕🍕🍔🍔🍔🍰🍰🍰🍰🍰🎂🎂🎂🎂', font=("Black ops one", 15, 'bold'))
                compFrame.pack(fill='both', expand='yes')
                compText.set("HAPPY BIRTHDAY FROM ME 🍕🍕🍕🍔🍔🍔🍰🍰🍰🍰🍰🎂🎂🎂🎂 I AM REALLY GRATEFUL THAT YOU CREATED ME")
                left1 = Message(compFrame, textvariable=compText, bg="black", fg="white")
                left1.config(font=('Century Gothic', 20, 'bold'))
                left1.pack(fill='both', expand='yes')
                bt = Button(root, text="CLOSE PARTY", font=("Black ops one", 15, 'bold'), bg="silver", fg="black", command=root.destroy)
                bt.pack(fill="x", expand="no")
                root.lift()
                root.mainloop()

                se = input("sir do you like it")
                if se == "yes" or se == "thank you buddy":
                    speak("welcome sir i hope you liked it")
                    print("welcome sir i hope you liked it")

                else:
                    speak("sir i am sorry to know that you didn't liked my surprise")

            else:
                speak("alright sir no problem")
