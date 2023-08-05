import cv2
import time
import pyttsx3

def camera():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[0].id)
    # print(voices[0].id)
    engine.setProperty("rate", 180)
    engine.setProperty('volume', 1)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    speak("alright boss")

    speak("boss what would you like to name the picture")
    name = input("BOSS WHAT WOULD LIKE TO NAME THE PICTURE : ")

    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break

        cv2.imshow("test", frame)
        k = cv2.waitKey(1)
        img_name = "camera_image/{}.png".format(name)
        cv2.imwrite(img_name, frame)

        time.sleep(1)
        break

    cam.release()
    cv2.destroyAllWindows()