from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from Tkinter import *

## Function used to login
def login(username,password):
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.ehlo()
    server.starttls()
    try:
        server.login(username,password)
        return(True)
    except:
        return(False)

## Fucntion to send mail
def sendmail(username,password,to_email,Subject,Message):
    from_address = username
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = Subject
    msg['From'] = from_address
    msg['To'] = to_email

    # Create the message (HTML).
    html = Message

    # Record the MIME type - text/html.
    part1 = MIMEText(html, 'html')

    # Attach parts into message container
    msg.attach(part1) 

    # Sending the email
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.ehlo()
    server.starttls()
    server.login(username,password)  
    server.sendmail(from_address, to_email, msg.as_string())  
    server.quit()
    return(True)