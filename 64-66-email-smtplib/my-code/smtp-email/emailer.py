#!python3
#emailer.py is a simple script for sending emails using smtplib

import smtplib
import os
from dotenv import load_dotenv

load_dotenv()



from_addr = '.@gmail.com'
to_addr = '.@gmail.com'
password = os.getenv("PASSWORD")

body = """New Releases and Sales on Steam
    
Click the links below to check them out!
   
"""

smtp_server = smtplib.SMTP('smtp.gmail.com', 587)

smtp_server.ehlo()

smtp_server.starttls()

smtp_server.login('.@gmail.com ', password)

smtp_server.sendmail(from_addr, to_addr, body)

smtp_server.quit()

print('Email sent successfully')