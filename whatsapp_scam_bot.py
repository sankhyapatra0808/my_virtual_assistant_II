import pyautogui as pg
import webbrowser
import time

print("THIS IS A SCAM BOT PLEASE USE IT CAREFULLY")

pg.click(x=447, y=723)

name = input("ENTER THE PERSON'S NAME TO BE SENT ")
print("OKEY DOKEY I WILL DO IT SIR")

webbrowser.open("https://web.whatsapp.com/")
time.sleep(20)

# maximizing window
pg.hotkey('alt', 'space')
pg.press("x")
time.sleep(1)

# search button
pg.click(x=299, y=220)
pg.typewrite(name)
time.sleep(3)

# name/number search
pg.click(x=354, y=395)
time.sleep(3)

for i in range(200):
    # type message
    pg.typewrite("i'm devil ;_;")
    # pg.typewrite("plz bro")
    time.sleep(0.2)
    # sending the message
    pg.click(x=1784, y=967)

# pg.click(x=1896, y=18)
