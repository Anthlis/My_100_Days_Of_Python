#!/usr/bin/python

import csv
import smtplib
import os
from email.mime.text import MIMEText
# from email.Header import Header
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()
password = os.getenv("PASSWORD")

def sendmail(info_list):
    msg = MIMEText(info_list[2], "html", "utf-8")
    msg['Subject'] = Header("A VERY IMPORTANT SUBJECT", "utf-8")
    msg['From'] = ".@gmail.com"
    msg['To'] = info_list[1]
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.ehlo()
    s.starttls()
    s.login(".@gmail.com", password)
    s.sendmail(".@gmail.com", info_list[1], msg.as_string())

def main():
    with open("msg.csv", "rb") as csvfile:
        msg_reader = csv.reader(csvfile)
        msg_reader.next()
        map(lambda x: sendmail(x), msg_reader)

if __name__ == "__main__":
    main()