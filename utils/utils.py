from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import ssl
import codecs
from random import randint
from datetime import datetime

port = 465

def add_log_error(error, mail):
    now = datetime.now()
    with open('log.txt', 'a') as file:
        file.write(f'{now.strftime("%d/%m/%Y %H:%M:%S")} | {mail} | ERROR: {error}\n')
    file.close()

def random_code():
    code = randint(000000, 999999)
    return code

def send_email(sender_name, sender_email, receiver_name, receiver_email, password, server):
    message = MIMEMultipart("alternative")
    message["Subject"] = "Account Activation"

    message["From"] = f"{sender_name} <{sender_email}>"
    message["To"] = f"{receiver_name} <{receiver_email}>"

    code = random_code()

    html_content = codecs.open("template/index.html")

    content = f"""\
    Logo
    Hello, {receiver_name}. Your confirmation code is:
    {code}
    Do not respond."""

    html = html_content.read().format(rec_name = receiver_name, rand_code = code)

    first_part = MIMEText(content, "plain")
    second_part = MIMEText(html, "html")

    fp = open("assets/ACompany.png", "rb")
    image = MIMEImage(fp.read())
    fp.close()

    image.add_header("Content-ID", "<ACompany>")
    message.attach(image)

    message.attach(first_part)
    message.attach(second_part)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(server, port, context=context) as server:
        try:
            server.login(sender_email, password)
            print(f"Sending email to {receiver_email}.")
        except smtplib.SMTPAuthenticationError as error:
            print(f"Unexpected {error}. The username or password is incorrect.\n")
            add_log_error(error, receiver_email)
        try:
            ret = server.sendmail(sender_email, receiver_email, message.as_string())
            if len(ret) == 0:
                print(f"Successfully sent to {receiver_email}.\n")
        except smtplib.SMTPRecipientsRefused as error:
            print(f"Unexpected {error}. The recipient address is invalid. No mail was sent.\n")
            add_log_error(error, receiver_email)
        except smtplib.SMTPSenderRefused as error:
            print(f"Unexpected {error}. There is something wrong with sender's mail address.\n")
            add_log_error(error, receiver_email)

        server.quit()