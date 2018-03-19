# -*- coding: utf-8 -*-
import os
import festWebsite.settings
from wsgiref.util import FileWrapper
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from website.models import Campus_Ambassdors, Sponsors, Team, Events, UserProfile, Pro_Night, single_event, \
    Team_details, event_register
from website.models import FestAccomodation
from website.forms import Campus_Ambassdor_Form, UserForm, UserProfileForm, FestAccomodationForm
from django.conf import settings
from django.core import mail
from django.core.mail import send_mail, EmailMessage
from django.test.utils import override_settings
from django.template.loader import get_template
from django.template import Context, Template, RequestContext
import datetime
import hashlib
# import pyqrcode
from django.contrib.auth import authenticate, login, logout
from random import randint
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    context_dict = {}
    return render(request, 'website/index.html', context_dict)


def home(request):
    context_dict = {}
    homepage = list(Events.objects.filter(type2="1"))
    context_dict['home_details'] = homepage
    return render(request, 'website/newhome.html', context_dict)


def success(request, context_dict):
    return render(request, 'website/Success.html', context_dict)


def contact(request):
    return render(request, 'website/contact.html')


def sponsor(request):
    return render(request, 'website/sponsors.html')


def current_sponsor(request):
    context_dict = {}
    title_sponsors = list(Sponsors.objects.filter(type="1"))
    normal_sponsors = list(Sponsors.objects.filter(type="3"))
    event_sponsors = list(Sponsors.objects.filter(type="4"))
    media_sponsors = list(Sponsors.objects.filter(type="2"))
    j = 0
    k = []
    ns = []
    for i in normal_sponsors:
        j += 1
        flag = 0
        k.append(i)
        if j % 3 == 0 or j == len(normal_sponsors):
            flag = 1
        if flag == 1:
            ns.append(k)
            k = []
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
    context_dict['ts'] = title_sponsors
    context_dict['ns'] = ns
    context_dict['es'] = es
    context_dict['ms'] = oms
    return render(request, 'website/current_sponsors.html', context_dict)


def team(request):
    context_dict = {}
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
    core1 = []
    core2 = []
    core3 = []
    for i in core:
        if i.position == "General Secretary":
            core1.append(i)
        elif i.position == "Overall Fest Coordinator":
            core2.append(i)
        elif i.position == "Deputy General Secretary":
            core3.append(i)
    core_main.append(core1)
    core_main.append(core2)
    core_main.append(core3)
    data = []
    data.append(core_main)
    sp = []
    sp_main = []
    for i in sponsorship:
        sp.append(i)
    sp_main.append(sp)
    data.append(sp_main)
    sp = []
    sp_main = []
    for i in design:
        sp.append(i)
    sp_main.append(sp)
    data.append(sp_main)
    sp = []
    sp_main = []
    for i in pr:
        sp.append(i)
    sp_main.append(sp)
    data.append(sp_main)
    sp = []
    sp_main = []
    for i in tm:
        sp.append(i)
    sp_main.append(sp)
    data.append(sp_main)
    sp = []
    sp_main = []
    for i in technical:
        sp.append(i)
    sp_main.append(sp)
    data.append(sp_main)
    sp = []
    sp_main = []
    for i in decoration:
        sp.append(i)
    sp_main.append(sp)
    data.append(sp_main)
    sp = []
    sp_main = []
    for i in social_media:
        sp.append(i)
    sp_main.append(sp)
    data.append(sp_main)
    sp = []
    sp_main = []
    for i in content_writing:
        sp.append(i)
    sp_main.append(sp)
    data.append(sp_main)
    sp = []
    sp_main = []
    for i in operation:
        sp.append(i)
    sp_main.append(sp)
    data.append(sp_main)
    types = [[1, 4, 2], [3], [2], [2], [2], [2], [2], [3], [3], [2]]
    headings = ["Core Team", "Sponsorship", "Design", "Public Relations", "Talent Management", "Technical",
                "Decoration", "Social Media Marketing", "Content Writing", "Operations"]
    zipped = zip(data, types, headings)
    context_dict['zipped'] = zipped
    return render(request, 'website/team.html', context_dict)


def show_event(request, event_name_slug):
    context_dict = {}
    event_details = list(Events.objects.filter(slug=event_name_slug))
    i = event_details[0]
    context_dict['rules'] = 1
    if i.rules == "":
        context_dict['rules'] = 0
    context_dict['prize'] = 1
    if i.prize == 0:
        context_dict['prize'] = 0
    k = str(i.rules)
    l = k.find("/")
    m = k[l + 1:]
    n = m.find(".")
    o = m[n + 1:]
    m = m[:n]
    spon = []
    if i.sponsor1 != "":
        spon.append(i.sponsor1)
    if i.sponsor2 != "":
        spon.append(i.sponsor2)
    if i.sponsor3 != "":
        spon.append(i.sponsor3)
    if i.sponsor4 != "":
        spon.append(i.sponsor4)
    if i.max_participants == 1:
        context_dict['single'] = 1
    else:
        context_dict['single'] = 0
    context_dict['event_details'] = event_details
    context_dict['file_name'] = m
    context_dict['extension'] = o
    context_dict['sponsors'] = spon
    context_dict['slug'] = event_name_slug
    return render(request, 'website/event1.html', context_dict)


def event_list(request):
    context_dict = {}
    flagship = list(Events.objects.filter(type1="F"))
    major = list(Events.objects.filter(type1="Ma"))
    minor = list(Events.objects.filter(type1="Mi"))
    context_dict['flagship'] = flagship
    context_dict['major'] = major
    context_dict['minor'] = minor
    return render(request, 'website/event_list.html', context_dict)


def campusambassador(request):
    form = Campus_Ambassdor_Form()
    context_dict = {}
    if request.method == 'POST':
        form = Campus_Ambassdor_Form(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            email = request.POST['email']
            phone = request.POST['phone']
            subject = "Greetings from 67th Milestone'18"
            body1 = u"Hi,\n\n" + \
                    u"Greetings from Team 67th Milestone'18 and welcome to our family. \n\n" + \
                    u"Thank you for applying to Campus Ambassador Internship. We are looking forward to" \
                    u" work with you and will get back to you soon regarding the onset of" \
                    u" the program once final applications are shortlisted.\n\n"
            body2 = u"All the best!"
            body3 = u"\n\nFor more updates, stay tuned on - \n\n" + \
                    u"Website - www.67thmilestone.com \n" + \
                    u"Facebook - www.facebook.com/67milestone\n" + \
                    u"Instagram - www.instagram.com/67thmilestone\n" + \
                    u"Twitter - www.twitter.com/67th_milestone\n"
            body = body1 + body2 + body3
            emailsend = EmailMessage(subject, body, to=[email])
            emailsend.send()
            page.save()
            print(phone, email)
            context_dict = {}
            context_dict['email'] = email
            context_dict['phone'] = phone
            return render(request, 'website/Success.html', context_dict)
        else:
            if 'email' in form.errors:
                context_dict['error'] = 'User with this Email already exits'
                print(context_dict)
            elif 'phone' in form.errors:
                context_dict['error'] = 'User with this Whatsapp Number already exits'
                print(context_dict)
            return render(request, 'website/error.html', context_dict)
    context_dict['form'] = form
    print(context_dict)
    return render(request, 'website/campusamb.html', context_dict)


def error(request):
    context_dict = {}
    return render(request, 'website/error.html', context_dict)


@login_required(login_url='/login/')
def download(request, file_name, extension):
    path1 = '/rules/' + file_name + "." + extension
    return HttpResponseRedirect('/media' + path1)


def gallery(request):
    context_dict = {}
    return render(request, 'website/gallery.html', context_dict)


@login_required(login_url='/login/')
def profile(request):
    context_dict = {}
    user_details = list(UserProfile.objects.filter(user=request.user))
    for i in user_details:
        context_dict['name'] = i.name
        context_dict['college'] = i.college
        context_dict['contact'] = i.contact
        context_dict['picture'] = i.picture
    context_dict['email'] = request.user.email
    events_registered = list(single_event.objects.filter(username=request.user.username))
    events_registered1 = list(event_register.objects.filter(username=request.user.username))
    events_registered_details1 = []
    for i in events_registered1:
        event_name = i.event_name
        event_details = list(Events.objects.filter(name=event_name))
        j = event_details[0]
        events_registered_details1.append(j)
    events_registered_details = []
    for i in events_registered:
        event = i.event_name
        event_details = list(Events.objects.filter(slug=event))
        j = event_details[0]
        events_registered_details.append(j)
    context_dict['registered_events'] = events_registered_details
    context_dict['registered_events1'] = events_registered_details1
    obj = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(request.POST or None, instance=obj)
    context_dict['form'] = form
    if request.method == "POST":
        if form.is_valid():
            obj = form.save(commit=False)
            print(obj.picture)
            if 'picture' in request.FILES:
                obj.picture = request.FILES['picture']
                print(request.FILES['picture'])
            obj.save()
            context_dict['form'] = form
            return HttpResponseRedirect('/profile')
        else:
            context_dict['form'] = form
            context_dict['error'] = 'The form was not updated successfully.'
            return render(request, 'website/profile.html', context_dict)
    return render(request, 'website/profile.html', context_dict)


@csrf_protect
@csrf_exempt
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            subject = "Greetings from 67th Milestone'18"
            body1 = u"Dear participant,\n\n" + \
                    u"Congratulations on successfully registering " + \
                    u"for 67th Milestone’18. We are delighted to host you at BML Munjal University from April 5-7, 2018. \nPlease keep checking our website for further updates.\n\n" + \
                    u"Please find below your login details –\n" + \
                    u"Username: "
            body2 = str(user.username)
            body3 = u"\n\nNote : No participant will be allowed to enter without College ID Card" + \
                    u"\n\nFor further details, refer to\n" + \
                    u"Facebook Page: https://www.facebook.com/67milestone/\n" + \
                    u"Instagram Page: https://www.instagram.com/67thmilestone/\n" + \
                    u"Aftermovie'17: https://www.youtube.com/watch?v=VG47-yBbebE\n" + \
                    u"Youtube Channel Page: https://www.youtube.com/channel/UC-8pUgtFwwfLHHWIDnXLTVw\n\n" + \
                    u"Regards,\n" + \
                    u"Team 67th Milestone"
            body = body1 + body2 + body3
            emailsend = EmailMessage(subject, body, to=[user.email])
            emailsend.send()
            registered = True
            return HttpResponseRedirect('/login')
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    context_dict = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}
    return render(request, 'website/login.html', context_dict)


@csrf_protect
@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect("Account Disabled")
        else:
            print("Invalid credentials: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details")
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        context_dict = {'user_form': user_form, 'profile_form': profile_form}
        return render(request, 'website/login.html', context_dict)


@login_required(login_url='/login/')
def user_logout(requset):
    logout(requset)
    return HttpResponseRedirect('/')


@login_required(login_url='/login/')
def editprofile(request):
    obj = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(request.POST or None, instance=obj)
    context = {'form': form}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        context = {'form': form}
        return render(request, 'website/edit.html', context)
    else:
        context = {'form': form,
                   'error': 'The form was not updated successfully.'}
        return render(request, 'website/edit.html', context)


def show_pronight(request, pro_night_name_slug):
    context_dict = {}
    pro_night_details = list(Pro_Night.objects.filter(slug=pro_night_name_slug))
    i = pro_night_details[0]
    context_dict['name'] = i.name
    context_dict['desc'] = i.description
    context_dict['image'] = i.main_image
    small_images = []
    if i.small_image_1 != "":
        small_images.append(i.small_image_1)
    if i.small_image_2 != "":
        small_images.append(i.small_image_2)
    if i.small_image_3 != "":
        small_images.append(i.small_image_3)
    if i.small_image_4 != "":
        small_images.append(i.small_image_4)
    if i.small_image_5 != "":
        small_images.append(i.small_image_5)
    if i.small_image_6 != "":
        small_images.append(i.small_image_6)
    if i.small_image_7 != "":
        small_images.append(i.small_image_7)
    if i.small_image_8 != "":
        small_images.append(i.small_image_8)
    if i.small_image_9 != "":
        small_images.append(i.small_image_9)
    if i.small_image_10 != "":
        small_images.append(i.small_image_10)
    if i.small_image_11 != "":
        small_images.append(i.small_image_11)
    if i.small_image_12 != "":
        small_images.append(i.small_image_12)
    if i.small_image_13 != "":
        small_images.append(i.small_image_13)
    if i.small_image_14 != "":
        small_images.append(i.small_image_14)
    if i.small_image_15 != "":
        small_images.append(i.small_image_15)
    large_images = []
    if i.large_image_1 != "":
        large_images.append(i.large_image_1)
    if i.large_image_2 != "":
        large_images.append(i.large_image_2)
    if i.large_image_3 != "":
        large_images.append(i.large_image_3)
    if i.large_image_4 != "":
        large_images.append(i.large_image_4)
    if i.large_image_5 != "":
        large_images.append(i.large_image_5)
    if i.large_image_6 != "":
        large_images.append(i.large_image_6)
    if i.large_image_7 != "":
        large_images.append(i.large_image_7)
    if i.large_image_8 != "":
        large_images.append(i.large_image_8)
    if i.large_image_9 != "":
        large_images.append(i.large_image_9)
    if i.large_image_10 != "":
        large_images.append(i.large_image_10)
    if i.large_image_11 != "":
        large_images.append(i.large_image_11)
    if i.large_image_12 != "":
        large_images.append(i.large_image_12)
    if i.large_image_13 != "":
        large_images.append(i.large_image_13)
    if i.large_image_14 != "":
        large_images.append(i.large_image_14)
    if i.large_image_15 != "":
        large_images.append(i.large_image_15)
    zipped_images = zip(small_images, large_images)
    context_dict['zipped_images'] = zipped_images
    return render(request, 'website/pronite.html', context_dict)


def hospitality(request):
    context_dict = {}
    return render(request, 'website/Hospitality.html', context_dict)


@login_required(login_url='/login/')
def single_event_register(request, event_name_slug):
    try:
        p = single_event(username=request.user.username, event_name=event_name_slug)
        p.save()
        event = list(Events.objects.filter(slug=event_name_slug))
        name_event = event[0].name
        date = event[0].date
        time = event[0].time
        subject = "Greetings from 67th Milestone'18"
        body = u"Dear participant,\n\n" + \
               u"Greetings from Team 67th Milestone!\n\n" + \
               u"We are delighted to confirm your presence for the festival. " + \
               u"You’ve been registered for the " + \
               str(name_event) + \
               u" scheduled on " + \
               u"(" + \
               str(date) + \
               u" and " + \
               str(time) + \
               u" for the Individual event Scheduled)" + \
               u". Fest Itinerary will be shared soon.\n" + \
               u"\n\nNote : No participant will be allowed to enter without College ID Card" + \
               u"\nNote – For assistance to all the participants, we will also be providing Shuttle Service from " + \
               u"IFFCO Chowk to BML Munjal University from April 4-8, 2018 at two time zones.\n" + \
               u"\nIFFCO Chowk to BMU: 9 a.m. and 5 p.m.\n" + \
               u"\nBMU to IFFCO Chowk: 11 a.m. and 7 p.m.\n" + \
               u"\nA minimal service charge will be fared for the transport services on the account of the frequency of passengers." + \
               u" Kindly validate your seating and you will be informed about the exact fare charges in a few days. Upon filling the form," + \
               u" you confirm yourself for availing the transportation service.\n" + \
               u"\nTo apply for the services, please fill the this form – https://goo.gl/forms/jQzmF09qLRnmDITV2\n\n" + \
               u"For further details, refer to\n" + \
               u"Facebook Page: https://www.facebook.com/67milestone/\n" + \
               u"Instagram Page: https://www.instagram.com/67thmilestone/\n" + \
               u"Aftermovie'17: https://www.youtube.com/watch?v=VG47-yBbebE\n" + \
               u"Youtube Channel Page: https://www.youtube.com/channel/UC-8pUgtFwwfLHHWIDnXLTVw\n\n" + \
               u"Regards,\n" + \
               u"Team 67th Milestone"
        emailsend = EmailMessage(subject, body, to=[request.user.email])
        gh = name_event + request.user.username
        path1 = settings.MEDIA_DIR
        path1 += "/qrcode/"
        path1 += (gh + ".svg")
        user_details = list(UserProfile.objects.filter(user=request.user))
        i = user_details[0]
        a = (
        str(name_event) + "\n" + "Name : " + str(i.name) + "\nE-mail : " + str(request.user.email) + "\nPhone : " + str(
            i.contact))
        print(name_event, i.name, i.contact)
        print(a)
        # ticket_no = pyqrcode.create(a)
        # ticket_no.svg(path1, scale=8)
        # emailsend.attach_file(path1)
        emailsend.send()
    except:
        return HttpResponseRedirect('/event/' + event_name_slug)
    return HttpResponseRedirect('/profile')


def complete_team(request):
    context_dict = {}
    return render(request, 'website/completeteam.html', context_dict)


@login_required(login_url='/login/')
def team_register(request, event_name_slug):
    flag = 0
    event = list(Events.objects.filter(slug=event_name_slug))
    name_event = event[0].name
    size = event[0].max_participants
    t = []
    for i in range(size):
        t.append(i)
    context = {'slug': event_name_slug, 'team_size': t}
    try:
        if request.method == 'POST':
            p = event_register(username=request.user.username, event_name=name_event,
                               team_name=request.POST.get('team_name'))
            p.save()
            body4 = "The details of your team is : \n"
            for i in range(0, size):
                if request.POST.get('name' + str(i)) != "" and request.POST.get('email' + str(i)) and request.POST.get(
                                'phone' + str(i)):
                    team = Team_details(name=request.POST.get('name' + str(i)), team_name=request.POST.get('team_name'),
                                        event_name=name_event, email=request.POST.get('email' + str(i)),
                                        phone=request.POST.get('phone' + str(i)))
                    body4 += request.POST.get('name' + str(i))
                    body4 += "\n"
                    team.save()
            flag = 1
            event = list(Events.objects.filter(slug=event_name_slug))
            name_event = event[0].name
            date = event[0].date
            time = event[0].time
            subject = "Greetings from 67th Milestone'18"
            body = u"Dear participant,\n\n" + \
                   u"Greetings from Team 67th Milestone!\n\n" + \
                   u"We are delighted to confirm your presence for the festival. " + \
                   u"You’ve been registered for the " + \
                   str(name_event) + \
                   u" scheduled on " + \
                   u"(" + \
                   str(date) + \
                   u" and " + \
                   str(time) + \
                   u" for the Team event Scheduled)" + \
                   u". Fest Itinerary will be shared soon.\n\n" + \
                   str(body4) + \
                   u"\n\nNote : \n" + \
                   u"No participant will be allowed to enter without College ID Card" + \
                   u"\nFor assistance to all the participants, we will also be providing Shuttle Service from " + \
                   u"IFFCO Chowk to BML Munjal University from April 4-8, 2018 at two time zones.\n" + \
                   u"\nIFFCO Chowk to BMU: 9 a.m. and 5 p.m.\n" + \
                   u"\nBMU to IFFCO Chowk: 11 a.m. and 7 p.m.\n" + \
                   u"\nA minimal service charge will be fared for the transport services on the account of the frequency of passengers." + \
                   u" Kindly validate your seating and you will be informed about the exact fare charges in a few days. Upon filling the form," + \
                   u" you confirm yourself for availing the transportation service.\n" + \
                   u"\nTo apply for the services, please fill the this form – https://goo.gl/forms/jQzmF09qLRnmDITV2\n\n" + \
                   u"For further details, refer to\n" + \
                   u"Facebook Page: https://www.facebook.com/67milestone/\n" + \
                   u"Instagram Page: https://www.instagram.com/67thmilestone/\n" + \
                   u"Aftermovie'17: https://www.youtube.com/watch?v=VG47-yBbebE\n" + \
                   u"Youtube Channel Page: https://www.youtube.com/channel/UC-8pUgtFwwfLHHWIDnXLTVw\n\n" + \
                   u"Regards,\n" + \
                   u"Team 67th Milestone"
            emailsend = EmailMessage(subject, body, to=[request.user.email])
            gh = name_event + request.user.username
            path1 = settings.MEDIA_DIR
            path1 += "/qrcode/"
            path1 += (gh + ".svg")
            user_details = list(UserProfile.objects.filter(user=request.user))
            i = user_details[0]
            a = (str(name_event) + "\n" + "Name : " + str(i.name) + "\nE-mail : " + str(
                request.user.email) + "\nPhone : " + str(i.contact))
            print(name_event, i.name, i.contact)
            print(a)
            # ticket_no = pyqrcode.create(a)
            # ticket_no.svg(path1, scale=8)
            # emailsend.attach_file(path1)
            emailsend.send()
    except:
        return HttpResponseRedirect('/event/' + event_name_slug)
    if flag == 0:
        return render(request, 'website/team_event.html', context)
    else:
        return HttpResponseRedirect('/profile')


@login_required(login_url='/login/')
def FestAccomodationView(request):
    context = {}
    if request.method == 'POST':
        form = FestAccomodationForm(request.POST)
        if form.is_valid():
            accomodate = form.save(commit=False)
            accomodate.user = request.user
            accomodate.save()
        else:
            print(form.errors)
    else:
        form = FestAccomodationForm()
    context['form'] = form
    return render(request, 'website/accomodation.html', context)

def mentor(request):
    context_dict = {}
    return render(request, 'website/Mentors.html', context_dict)