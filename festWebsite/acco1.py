#!/usr/bin/python3
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'festWebsite.settings')
import django

django.setup()
import pandas as pa
import csv

from website.models import FestAccomodation,User,UserProfile, Payment_Status
from django.core.mail import send_mail, EmailMessage
from django.conf import settings


def create():
    a = list(FestAccomodation.objects.all())
    labels = ['Name', 'College Name', 'Contact Number', 'Gender','Day1',
              'Day2','Day3','Day4','Expected Date','Expected Time','Payment_Status']
    c = []
    for i in a:
        d = []
        b = list(UserProfile.objects.filter(user=i.user))
        for j in b:
            d.append(j.name)
            d.append(j.college)
            d.append(j.contact)
            if j.gender == '0':
                d.append("Female")
            elif j.gender == '1':
                d.append("Male")
            elif j.gender == '2':
                d.append("Other")
        d.append(i.day1)
        d.append(i.day2)
        d.append(i.day3)
        d.append(i.day4)
        d.append(i.date)
        d.append(i.time)
        ps = list(Payment_Status.objects.all())
        flag = 0
        for ps1 in ps:
            if ps1.username == i.username:
                d.append(ps1.payment)
                flag = 1
        if flag == 0:
            d.append("NO")
        c.append(d)
    print(c)
    d = []
    for i in c:
        if len(i) > 0:
            d.append(i)
    print(d)
    df = pa.DataFrame(d, columns=labels)
    df.to_csv("Accommodations1.csv")
    subject = "Accommodation File"
    body = u"Find the attached CSV File for accommodations."
    '''emailsend = EmailMessage(subject, body, to=['tushar.bhatia.15csc@bml.edu.in', 'sankalp.pasricha.15csc@bml.edu.in',
          'danish.jameel.15csc@bml.edu.in', 'dadu.reddy.15ece@bml.edu.in',
          'manav.gupta.15cse@bml.edu.in', 'astha.sharma.16mec@bml.edu.in',
          'mahima.chopra.15csc@bml.edu.in', 'nishit.garg.15csc@bml.edu.in',
          'k.natasha.15bck@bml.edu.in', 'shreya.mathur.15bk@bml.edu.in'])'''
    emailsend = EmailMessage(subject, body, to=['pprashant2398@gmail.com'])
    path = os.getcwd()
    path += "/Accommodations1.csv"
    print(path)
    emailsend.attach_file(path)
    emailsend.send()
    print(df)


if __name__ == "__main__":
    print("Starting fetching database : ")
    create()