import smtplib     ### simple mail trnsfer protocol library


sender = input("Enter sender's email ID: ")
receiver = input("Enter receiver's email ID: ")
password = input("Enter your password: ")
subject = input("Enter the subject: ")
body = input("Enter the body: ")

### header

messsage = f""" From: Chijith Jerin{sender}
To: Benny Jarvish{receiver}
Subject: {subject}

{body}
"""


server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()   ## transport layer security

try:
    server.login(sender,password)
    print("Logged in....")
    server.sendmail(sender,receiver,messsage)
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError:
    print("unable to sign in")