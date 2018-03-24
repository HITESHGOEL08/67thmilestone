"""festWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from website import views

urlpatterns = [
    url(r'^bmladmin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^campusambassador',views.campusambassador,name='campusambassador'),
    url(r'^success/$',views.success,name='success'),
    url(r'^error/$',views.error,name='error'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^sponsor/$', views.sponsor, name='sponsor'),
    url(r'^current_sponsor/$',views.current_sponsor,name='current_sponsor'),
    url(r'^team/$', views.team,name='team'),
    url(r'^event/(?P<event_name_slug>[\w\-]+)/$', views.show_event,name='show_event'),
    url(r'^pro_night/(?P<pro_night_name_slug>[\w\-]+)/$', views.show_pronight,name='show_pro_night'),
    url(r'^event/$',views.event_list,name='event_list'),
    url(r'^download/(?P<file_name>[\w\-]+)/(?P<extension>[\w\-]+)', views.download,name='download'),
    url(r'^gallery/$', views.gallery,name='gallery'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^(?P<event_name_slug>[\w\-]+)/register/$', views.single_event_register, name='single_event_register'),
    url(r'^(?P<event_name_slug>[\w\-]+)/team_register/$', views.team_register, name='team_register'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^edit', views.editprofile, name='edit'),
    url(r'^hospitality/$', views.hospitality, name='Hospitality'),
    url(r'^complete_team/$', views.complete_team, name='complete_team'),
    url(r'^mentors/$', views.mentor, name='mentor'),
    url(r'^payment/(?P<event_name_slug>[\w\-]+)', views.payment, name='payment'),
    url(r'^payment_success/(?P<event_name_slug>[\w\-]+)/(?P<username>[\w\-]+)', views.payment_success, name='payment_success'),
    url(r'^payment_failure/(?P<event_name_slug>[\w\-]+)', views.payment_failure, name='payment_failure'),
]