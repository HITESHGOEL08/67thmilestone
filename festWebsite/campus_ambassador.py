import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'festWebsite.settings')
import django

django.setup()
import pandas as pa
import csv

from website.models import Campus_Ambassdors
from django.core.mail import send_mail, EmailMessage
from django.conf import settings


def create():
    a = list(Campus_Ambassdors.objects.all().values_list())
    labels = ['ID', 'Name', 'Email', 'Phone', 'College Name', 'College Address', 'CA Code', 'Reason']
    b = []
    for i in range(0, len(a)):
        b.append(a[i][0:8])
    df = pa.DataFrame.from_records(b, columns=labels)
    df.index = df['ID']
    df.to_csv("Campus_Ambassadors.csv")
    subject = "Responses for Campus Ambassador Form(67th Milestone'18)"
    body = u"Find the attached CSV File for registered campus ambassadors."
    emailsend = EmailMessage(subject, body, to=['hiteshgoel426@gmail.com'])
    path = os.path.dirname(__file__)
    path += "/Campus_Ambassadors.csv"
    print(path)
    emailsend.attach_file(path)
    emailsend.send()
    print(df)


if __name__ == "__main__":
    print("Starting fetching database : ")
    create()
