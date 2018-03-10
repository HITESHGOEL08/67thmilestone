import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'festWebsite.settings')
import django

django.setup()
import pandas as pa
import csv
import pyqrcode
from website.models import Campus_Ambassdors
from django.core.mail import send_mail, EmailMessage
from django.conf import settings


def create():
    body = "Congrats\n"

    body1 = "check the mail"
    body2 = body + body1
    print(body2)
    ticket_no = pyqrcode.create(body2)

    subject = "Responses for Campus Ambassador Form(67th Milestone'18)"
    emailsend = EmailMessage(subject, body2, to=['nishit.garg.15csc@bml.edu.in'])

    print(settings.MEDIA_DIR)

    gh="jhjjjj"
    path1 = settings.MEDIA_DIR
    path1 +="/qrcode/"
    path1+=gh+".svg"
    ticket_no.svg(path1, scale=8)
    path = os.path.dirname(path1+'a.svg')

    emailsend.attach_file(path)
    emailsend.send()


if __name__ == "__main__":
    print("Starting creating qrcode : \n sending")
    create()
