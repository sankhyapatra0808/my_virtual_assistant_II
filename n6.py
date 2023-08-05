import smtplib
import ssl
from email.message import EmailMessage

def send_email_message():


    # Define email sender and receiver
    email_sender = "sankhyapatra0808@gmail.com"
    email_password = 'lncmvmoynubutqxf'
    email_receiver = "asim2742004@gmail.com"

    # Set the subject and body of the email

    subject = input("Enter the subject you want to send : ")

    body = input("Enter the body's text you want to send : ")

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
send_email_message()