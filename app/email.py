from flask_mail import Message
from flask import render_template
from . import mail

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def mail_message(subject,template,to,**kwargs):
    sender_email = 'jtwiceo@gmail.com'

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)