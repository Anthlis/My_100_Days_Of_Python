#!python3
# emailer.py is a simple script for sending emails using smtplib

import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()
password = os.getenv("PASSWORD")

from_addr = '.@gmail.com'
to_addr = ''
bcc = ['.@outlook.com', '@gmail.com', '@yahoo.co.nz']

msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = 'MIME email (2) sent from PyCharm'

body = """I can send email from a Python3 script. 

I want to see if the BCC email addresses can be seen by everyone.

DELETE ME. 

"""

msg.attach(MIMEText(body, 'plain'))

smtp_server = smtplib.SMTP('smtp.gmail.com', 587)

smtp_server.ehlo()

smtp_server.starttls()

smtp_server.login(' .@gmail.com ',  password)

text = msg.as_string()

smtp_server.sendmail(from_addr, [to_addr] + bcc, text)

smtp_server.quit()

print('Email sent successfully')