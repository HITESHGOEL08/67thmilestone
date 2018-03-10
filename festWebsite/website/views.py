# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django import forms
from django.http import HttpResponse
from website.models import Campus_Ambassdors,Sponsors,Team
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

def current_sponsor(request):
    context_dict={}
    title_sponsors = list(Sponsors.objects.filter(type="1"))
    normal_sponsors = list(Sponsors.objects.filter(type="3"))
    event_sponsors = list(Sponsors.objects.filter(type="4"))
    media_sponsors = list(Sponsors.objects.filter(type="2"))
    j=0
    k=[]
    ns=[]
    for i in normal_sponsors:
        j+=1
        flag = 0
        k.append(i)
        if j%3==0 or j == len(normal_sponsors):
            flag=1
        if flag==1:
            ns.append(k)
            k=[]
    j = 0
    k = []
    oms = []
    for i in media_sponsors:
        j += 1
        flag = 0
        k.append(i)
        if j % 3 == 0 or j == len(media_sponsors):
            flag = 1
        if flag == 1:
            oms.append(k)
            k = []
    j = 0
    k = []
    es = []
    for i in event_sponsors:
        j += 1
        flag = 0
        k.append(i)
        if j % 6 == 0 or j == len(event_sponsors):
            flag = 1
        if flag == 1:
            es.append(k)
            k = []
    context_dict['ts']=title_sponsors
    context_dict['ns']=ns
    context_dict['es']=es
    context_dict['ms']=oms
    return render(request, 'website/current_sponsors.html', context_dict)

def team(request):
    context_dict={}
    core = list(Team.objects.filter(type="1"))
    sponsorship = list(Team.objects.filter(type="2"))
    design = list(Team.objects.filter(type="3"))
    pr = list(Team.objects.filter(type="4"))
    tm = list(Team.objects.filter(type="5"))
    technical = list(Team.objects.filter(type="6"))
    operation = list(Team.objects.filter(type="7"))
    decoration = list(Team.objects.filter(type="8"))
    social_media = list(Team.objects.filter(type="9"))
    content_writing = list(Team.objects.filter(type="10"))
    core_main = []
    core1=[]
    core2=[]
    core3=[]
    for i in core:
        if i.position == "General Secretary":
            core1.append(i)
        elif i.position == "Fest Coordinators":
            core2.append(i)
        elif i.position == "Deputy General Secretary":
            core3.append(i)
    core_main.append(core1)
    core_main.append(core2)
    core_main.append(core3)
    data=[]
    data.append(core_main)
    data.append(sponsorship)
    data.append(design)
    data.append(pr)
    data.append(tm)
    data.append(technical)
    data.append(operation)
    data.append(decoration)
    data.append(social_media)
    data.append(content_writing)
    types=[[1,3,3],[3],[2],[2],[2],[2],[2],[2],[3],[2]]
    headings=["Core Team","Sponsorship","Design","PR","TM","Technical","Operation","Decoration","Social Media Marketing","Content Writing"]
    zipped = zip(data,types,headings)
    context_dict['zipped']=zipped
    return render(request,'website/team.html',context_dict)

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

def gallery(request):
    context_dict = {}
    return render(request, 'website/gallery.html', context_dict)