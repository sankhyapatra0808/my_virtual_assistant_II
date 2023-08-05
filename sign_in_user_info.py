import os
import cv2
import face_recognition
import JARVIS
import present_face_reader
import mysql.connector

def register_users():
    a = ""
    present_face_reader.present_face()
    path = r"C:\Users\user\PycharmProjects\AI_virtual_assistant_mark_II\Real_Image"
    for image in os.listdir(path):

        img1 = face_recognition.load_image_file("Real_Image/" + image)
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
        u_name = image[:-4].capitalize()
        a = a + str(results[0])

    if str(True) in a:
        user_name = u_name
        con = mysql.connector.connect(host="localhost", user="root", password="spaytm17", database="virtual_assistant")
        cur = con.cursor()
        q = "select * from jarvis inner join jarvis_user_name on jarvis_user_name.email = jarvis.email WHERE user_name = '" + user_name + "'"
        cur.execute(q)
        d = cur.fetchone()
        if d[3] == 'Male' or d[3] == 'M':
            print("Login information verified for Mr. " + d[0] + ", Welcome!!")
            name = d[0]
            email = d[1]
            password = d[2]
            gender = d[3]
            user_name = d[5]
            os.remove("Testing_image/test_image.jpg")
            return name, email, password, gender, user_name
        else:
            print("Login information verified for Hello Mrs. " + d[0] + ", Welcome!!")
            name = d[0]
            email = d[1]
            password = d[2]
            gender = d[3]
            user_name = d[5]
            os.remove("Testing_image/test_image.jpg")
            return name, email, password, gender, user_name

    else:
        print("Sorry you dont belong here for the first time. Please login again")
        JARVIS.start_of_jarvis()

