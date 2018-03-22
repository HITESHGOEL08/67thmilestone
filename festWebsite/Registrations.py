import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'festWebsite.settings')
import django

django.setup()
import pandas as pa
import csv

from website.models import Campus_Ambassdors, UserProfile, User
from django.core.mail import send_mail, EmailMessage
from django.conf import settings


def create():
    a = list(User.objects.all())
    labels = ['Name', 'Email', 'Username', 'College Name', 'Contact Number', 'Gender']
    c = []
    for i in a:
        d = []
        b = list(UserProfile.objects.filter(user=i))
        for j in b:
            d.append(j.name)
            d.append(i.email)
            d.append(i.username)
            d.append(j.college)
            d.append(j.contact)
            if j.gender == '0':
                d.append("Female")
            elif j.gender == '1':
                d.append("Male")
            elif j.gender == '2':
                d.append("Other")
        c.append(d)
    print(c)
    d = []
    for i in c:
        if len(i) > 0:
            d.append(i)
    print(d)
    df = pa.DataFrame(d, columns=labels)
    df.to_csv("Registrations.csv")
    subject = "Registration File"
    body = u"Find the attached CSV File for registered participants."
    emailsend = EmailMessage(subject, body, to=['tushar.bhatia.15csc@bml.edu.in', 'sankalp.pasricha.15csc@bml.edu.in',
                                                'danish.jameel.15csc@bml.edu.in', 'dadu.reddy.15ece@bml.edu.in',
                                                'manav.gupta.15cse@bml.edu.in', 'astha.sharma.16mec@bml.edu.in',
                                                'mahima.chopra.15csc@bml.edu.in', 'nishit.garg.15csc@bml.edu.in',
                                                'natasha.dora.15bck@bml.edu.in', 'shreya.mathur.15bk@bml.edu.in'])
    path = os.getcwd()
    path += "/Registrations.csv"
    print(path)
    emailsend.attach_file(path)
    emailsend.send()
    print(df)


if __name__ == "__main__":
    print("Starting fetching database : ")
    create()
