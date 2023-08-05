import smtplib
import ssl
from email.message import EmailMessage
import random
import face_reader
import internet_speed_tester

def otp():
    internet_speed_tester.speed_check()

    f = face_reader.face_reader()

    try:
        # Define email sender and receiver
        email_sender = f[2]
        email_password = 'lncmvmoynubutqxf'
        email_receiver = f[2]

        if "@" in email_receiver and ".com" in email_receiver and "@" in email_sender and ".com" in email_sender:
            l1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
            choice = random.choice(l1) + random.choice(l1) + random.choice(l1) + random.choice(l1) + random.choice(l1) + random.choice(l1) + random.choice(l1) + random.choice(l1)
            # Set the subject and body of the email
            subject = "NO-REPLY TO THIS EMAIL THIS IS AN OTP"
            body = "YOUR OTP FOR YOUR ACCOUNT IN J.A.R.V.I.S MARK I IS ' " + choice + " ' AND PLEASE DONT REPLY IN THIS EMAIL \nREMEMBER NOT TO SHARE YOUR OTP TO ANYONE"

            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['Subject'] = subject
            em.set_content(body)

            # Add SSL (layer of security)
            context = ssl.create_default_context()

            # Log in and send the email
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())

            print("Sent OTP to", f[1])
            print("DONE")
            print("PLEASE OPEN YOUR EMAIL TO RECEIVE THE OTP")

            ch = input("PLEASE ENTER THE OTP : ")
            if choice == ch:
                user_name = f[0]
                name = f[1]
                email = f[2]
                password = f[3]
                gender = f[4]
                return user_name, name, email, password, gender

    except:
        print("ERROR: Unable to process")

