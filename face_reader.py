import os
import new_registration
import cv2
import face_recognition
import present_face_reader
import mysql.connector

def face_reader():
    try:
        e = new_registration.new_registration_faces()

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

            if results == [True]:
                user_name = image[:-4].capitalize()
                con = mysql.connector.connect(host="localhost", user="root", password="spaytm17", database="virtual_assistant")
                cur = con.cursor()
                q = "select name from jarvis inner join jarvis_user_name on jarvis_user_name.email = jarvis.email WHERE user_name = '" + user_name + "'"
                cur.execute(q)
                d = cur.fetchone()
                if e[4] == 'Male' or e[4] == 'M':
                    print("Hello Mr. " + d[0] + ", Welcome!!")
                    user_name = e[0]
                    name = e[1]
                    email = e[2]
                    password = e[3]
                    gender = e[4]
                    os.remove("Testing_image/test_image.jpg")
                    return user_name, name, email, password, gender

                else:
                    print("Hello Mrs. " + d[0] + ", Welcome!!")
                    user_name = e[0]
                    name = e[1]
                    email = e[2]
                    password = e[3]
                    gender = e[4]
                    os.remove("Testing_image/test_image.jpg")
                    return user_name, name, email, password, gender

    except:
        print("Error in face reader please run again")
