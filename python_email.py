from cgitb import html
from email import message
import ssl
import smtplib
import ssl
from email.message import EmailMessage

subject = "Email frompython"
body = "this is a test email from python"
sender_email = "shubhampatni88@gmail.com"
receiver_email = "shubhampatni88@gmail.com"
password = input("Enter password : " )

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
#message.set_content(body)


html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <div>
            <p>{body}</p>
        </div>
    </body>
</html>
"""
message.add_alternative( html, subtype ="html" ) 

context = ssl.create_default_context()

print("Sending Email!")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email,receiver_email,message.as_string())

print("Success")