from django.db import models
from django.template.defaultfilters import slugify
from datetime import datetime
# Create your models here.
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    choice = (('0', 'Female'), ('1', 'Male'), ('2', 'Other'))
    college = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    gender = models.CharField(max_length=6, choices=choice)
    contact = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=30)
    Terms_and_Conditions = models.BooleanField()
    def __unicode__(self):
        return self.user.username

class Campus_Ambassdors(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    phone=models.BigIntegerField(unique=True)
    college_name=models.CharField(max_length=100)
    college_address=models.CharField(max_length=300)
    ca_code = models.CharField(max_length=50)
    reason_ca = models.CharField(max_length=500)
    slug = models.SlugField(unique=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.email)
        super(Campus_Ambassdors,self).save(*args,**kwargs)
    class Meta:
        verbose_name_plural = "Campus Ambassdors"
    def __str__(self):
        return self.name

class Sponsors(models.Model):
    choice = (("1","Title Sponsor"),("2","Online Media Sponsors"),("3","Normal Sponsor"),("4","Event Sponsor"))
    type = models.CharField(max_length=20,choices=choice)
    name = models.CharField(max_length=30,default="")
    name_shown = models.CharField(max_length=30,default="")
    image = models.ImageField(upload_to='sponsors', blank=True)
    url = models.URLField(default="")

    class Meta:
        verbose_name_plural = "Sponsors"
    def __str__(self):
        return self.name

class Team(models.Model):
    choice = (("1","Core"),("2","Sponsorship"),("3","Design"),("4","PR"),("5","TM"),("6","Technical"),("7","Operation"),\
              ("8","Decoration"),("9","Social Media"),("10","Content Writing"))
    type = models.CharField(max_length=20,choices=choice)
    name = models.CharField(max_length=30,default="")
    facebook = models.URLField(default="")
    instagram = models.URLField(default="")
    linkedin = models.URLField(default="")
    email = models.EmailField(default="")
    image = models.ImageField(upload_to='team', blank=True)
    position = models.CharField(max_length=30,default="")
    tag_line = models.CharField(max_length=100,default="")
    class Meta:
        verbose_name_plural = "Team"
    def __str__(self):
        return self.name

# class Register():
#     name = models.CharField(max_length=100, default="")
#     email = models.EmailField(max_length=100, unique=True)
#     phone = models.BigIntegerField(unique=True)
#     college_name = models.CharField(max_length=100)
#     choice = (("M","Male"),("F","Female"),("O","Other"))
#     gender = models.CharField(max_length=6,choices=choice)
#     image = models.ImageField(upload_to='profile_images', blank=True)
#     class Meta:
#         verbose_name_plural = "Register"
#     def __str__(self):
#         return self.name

class Event(models.Model):
    name = models.CharField(max_length=50,default="")
    choice = (("Technical","Technical"),("Cultural","Cultural"),("Management","Management"))
    type = models.CharField(max_length=30, choices=choice)
    choice_type = (("F","Flagship"),("Ma","Major"),("Mi","Minor"))
    type1 = models.CharField(max_length=30, choices=choice_type, default="F")
    choice_home=(("1","Home"),("2","NO"))
    type2 = models.CharField(max_length=10, choices = choice_home, default="2")
    fee = models.IntegerField()
    min_participants = models.IntegerField()
    max_participants = models.IntegerField()
    prize = models.IntegerField()
    image = models.ImageField(upload_to='events_logo', blank=True)
    description = models.CharField(max_length=500, default="")
    time = models.TimeField()
    date = models.DateField(default=datetime.now)
    venue = models.CharField(max_length=10)
    contact_name1 = models.CharField(max_length=30, default="")
    contact_phone1 = models.BigIntegerField(unique=True)
    contact_image1 = models.ImageField(upload_to='event_contact', blank=True)
    contact_email1 = models.EmailField(default="")
    contact_name2 = models.CharField(max_length=30, default="")
    contact_phone2 = models.BigIntegerField(unique=True)
    contact_image2 = models.ImageField(upload_to='event_contact', blank=True)
    contact_email2 = models.EmailField(default="")
    rules = models.FileField(upload_to='rules', blank=True)
    sponsor1 = models.ImageField(upload_to='events_sponsors', blank=True)
    sponsor2 = models.ImageField(upload_to='events_sponsors', blank=True)
    sponsor3 = models.ImageField(upload_to='events_sponsors', blank=True)
    sponsor4 = models.ImageField(upload_to='events_sponsors', blank=True)
    one_liner = models.CharField(max_length=100, default="")
    slug = models.SlugField(unique=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Event,self).save(*args,**kwargs)
    class Meta:
        verbose_name_plural = "Event"
    def __str__(self):
        return self.name

class Pro_Night(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    main_image= models.ImageField(upload_to='pro_nights', blank=True)
    small_image_1 = models.ImageField(upload_to='pro_nights', blank=True)
    small_image_2 = models.ImageField(upload_to='pro_nights', blank=True)
    small_image_3 = models.ImageField(upload_to='pro_nights', blank=True)
    small_image_4 = models.ImageField(upload_to='pro_nights', blank=True)
    small_image_5 = models.ImageField(upload_to='pro_nights', blank=True)
    small_image_6 = models.ImageField(upload_to='pro_nights', blank=True)
    small_image_7 = models.ImageField(upload_to='pro_nights', blank=True)
    small_image_8 = models.ImageField(upload_to='pro_nights', blank=True)
    small_image_9 = models.ImageField(upload_to='pro_nights', blank=True)
    small_image_10 = models.ImageField(upload_to='pro_nights', blank=True)
    small_image_11 = models.ImageField(upload_to='pro_nights', blank=True)
    small_image_12 = models.ImageField(upload_to='pro_nights', blank=True)
    small_image_13 = models.ImageField(upload_to='pro_nights', blank=True)
    small_image_14 = models.ImageField(upload_to='pro_nights', blank=True)
    small_image_15 = models.ImageField(upload_to='pro_nights', blank=True)
    large_image_1 = models.ImageField(upload_to='pro_nights', blank=True)
    large_image_2 = models.ImageField(upload_to='pro_nights', blank=True)
    large_image_3 = models.ImageField(upload_to='pro_nights', blank=True)
    large_image_4 = models.ImageField(upload_to='pro_nights', blank=True)
    large_image_5 = models.ImageField(upload_to='pro_nights', blank=True)
    large_image_6 = models.ImageField(upload_to='pro_nights', blank=True)
    large_image_7 = models.ImageField(upload_to='pro_nights', blank=True)
    large_image_8 = models.ImageField(upload_to='pro_nights', blank=True)
    large_image_9 = models.ImageField(upload_to='pro_nights', blank=True)
    large_image_10 = models.ImageField(upload_to='pro_nights', blank=True)
    large_image_11 = models.ImageField(upload_to='pro_nights', blank=True)
    large_image_12 = models.ImageField(upload_to='pro_nights', blank=True)
    large_image_13 = models.ImageField(upload_to='pro_nights', blank=True)
    large_image_14 = models.ImageField(upload_to='pro_nights', blank=True)
    large_image_15 = models.ImageField(upload_to='pro_nights', blank=True)
    slug = models.SlugField(unique=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Pro_Night,self).save(*args,**kwargs)
    class Meta:
        verbose_name_plural = "Pro_Night"
    def __str__(self):
        return self.name

class single_event(models.Model):
    username = models.CharField(max_length=30)
    event_name = models.CharField(max_length=30)
    class Meta:
        unique_together = ('username','event_name')