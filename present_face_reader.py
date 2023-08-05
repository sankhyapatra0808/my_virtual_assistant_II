def present_face():
    import cv2
    cam = cv2.VideoCapture(0)
    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break

        cv2.imshow("test", frame)
        k = cv2.waitKey(1)
        img_name = "Testing_image/test_image.jpg"
        cv2.imwrite(img_name, frame)
        break

    cam.release()
    cv2.destroyAllWindows()
