from flask_mail import Message
from app import app, mail
from threading import Thread


def async_email(app,msg):
    with app.app_context():
        mail.send(msg)



def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)
    Thread(target=async_email, args=(app, msg)).start()


