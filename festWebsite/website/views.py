# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django import forms
from django.http import HttpResponse
from website.models import Campus_Ambassdors
from website.forms import Campus_Ambassdor_Form
from django.conf import settings
from django.core.mail import send_mail,EmailMessage

# Create your views here.
def index(request):
    context_dict = {}
    return render(request, 'website/index.html', context_dict)


def success(request,context_dict):
    return render(request, 'website/Success.html', context_dict)


def contact(request):
    return render(request, 'website/contact.html')

def sponsor(request):
    return render(request, 'website/sponsors.html')

def campusambassador(request):
    form = Campus_Ambassdor_Form()
    context_dict={}
    if request.method == 'POST':
        form = Campus_Ambassdor_Form(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            email = request.POST['email']
            phone = request.POST['phone']
            subject = "Greetings from 67th Milestone'18"
            body1 = u"Hi,\n\n"+\
                   u"Greetings from Team 67th Milestone'18 and welcome to our family. \n\n" +\
                   u"Thank you for applying to Campus Ambassador Internship. We are looking forward to" \
                   u" work with you and will get back to you soon regarding the onset of" \
                   u" the program once final applications are shortlisted.\n\n"
            body2= u"All the best!"
            body3=u"\n\nFor more updates, stay tuned on - \n\n"+\
                   u"Website - www.67thmilestone.com \n"+\
                   u"Facebook - www.facebook.com/67milestone\n"+\
                   u"Instagram - www.instagram.com/67thmilestone\n"+\
                   u"Twitter - www.twitter.com/67th_milestone\n"
            body=body1+body2+body3
            emailsend = EmailMessage(subject,body,to=[email])
            emailsend.send()
            page.save()
            print(phone,email)
            context_dict={}
            context_dict['email']=email
            context_dict['phone']=phone
            return render(request, 'website/Success.html', context_dict)
        else:
            if 'email' in form.errors:
                context_dict['error'] = 'User with this Email already exits'
                print(context_dict)
            elif 'phone' in form.errors:
                context_dict['error'] = 'User with this Whatsapp Number already exits'
                print(context_dict)
            return render(request, 'website/error.html', context_dict)
    context_dict['form']=form
    print(context_dict)
    return render(request, 'website/campusamb.html', context_dict)

def error(request):
    context_dict = {}
    return render(request, 'website/error.html', context_dict)
