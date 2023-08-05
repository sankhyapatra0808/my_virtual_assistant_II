def new_registration_faces():
    import cv2
    import home_page
    import login_page

    a = home_page.first()
    b = login_page.login_page()

    if b[5] == 'y' or b[5] == 'yes':
        # a = input("OK SIR PLEASE ENTER YOUR NAME: ").lower()
        user_name = b[0]
        name = b[1]
        email = b[2]
        password = b[3]
        gender = b[4]
        print("YOUR DETAILS ARE HERE:- \nUser Name: " + user_name + ",\nName: " + name + ",\nEmail: " + email + ",\nPassword: " + password + ",\nGender: " + gender + ".")
        cam = cv2.VideoCapture(0)
        while True:
            ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")
                break

            cv2.imshow("test", frame)
            k = cv2.waitKey(1)
            img_name = "Real_Image/{}.jpg".format(user_name)
            img_name = "recogniser_image/{}.jpg".format(name)
            cv2.imwrite(img_name, frame)
            break
        return user_name, name, email, password, gender
        exit()
        cam.release()
        cv2.destroyAllWindows()

    else:
        user_name = b[0]
        name = b[1]
        email = b[2]
        password = b[3]
        gender = b[4]

        return user_name, name, email, password, gender

