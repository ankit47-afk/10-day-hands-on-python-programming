# how to send email through python .
import smtplib # this lib is used to send and reciving emails 
import ssl # ssl is used to make secure circuit 
from email.message import EmailMessage # means 
EMAIL = ""
APP_PASSWORD = ""
RECEIVER = ""
msg = EmailMessage()
msg["From"] = EMAIL
msg["To"] = RECEIVER
msg["Subject"] = " hi my name is ankit "
msg.set_content("this email is changed by pytho code ...")
context =ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(EMAIL, APP_PASSWORD)
    server.send_message(msg)

    
