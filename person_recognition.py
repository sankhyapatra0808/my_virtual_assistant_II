import os
import cv2
import face_recognition
import present_face_reader
import pyttsx3

def register_users():
    a = ""
    present_face_reader.present_face()

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[0].id)
    # print(voices[0].id)
    engine.setProperty("rate", 180)
    engine.setProperty('volume', 1)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    speak("Alright boss gimme a second")
    path = r"C:\Users\user\PycharmProjects\AI_virtual_assistant_mark_II\recogniser_image"
    for image in os.listdir(path):

        img1 = face_recognition.load_image_file("recogniser_image/" + image)
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

        img2 = face_recognition.load_image_file("Testing_image/test_image.jpg")
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

        face_loc = face_recognition.face_locations(img1)[0]
        encoding_img_1 = face_recognition.face_encodings(img1)[0]
        cv2.rectangle(img1, (face_loc[3], face_loc[0]), (face_loc[1], face_loc[2]), (255, 0, 255), 2)

        face_loc2 = face_recognition.face_locations(img2)[0]
        encoding_img_2 = face_recognition.face_encodings(img2)[0]
        cv2.rectangle(img2, (face_loc2[3], face_loc2[0]), (face_loc2[1], face_loc2[2]), (255, 0, 255), 2)

        results = face_recognition.compare_faces([encoding_img_1], encoding_img_2)
        name = image[:-4].capitalize()
        a = a + str(results[0])

    if str(True) in a:
        speak("I recognise you, you are " + name)
        print("I recognise you, you are " + name)
        os.remove("Testing_image/test_image.jpg")

    else:
        speak("Sorry you dont belong here for the first time. Please login first")
        print("Sorry you dont belong here for the first time. Please login first")
