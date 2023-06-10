import smtplib
import ssl
import os


def sendMail(message):
    host = "smtp.gmail.com"
    port = 465

    username = "addmarful@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "addmarful@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(username, password)
        server.sendmail(from_addr=username, to_addrs=receiver, msg=message)
