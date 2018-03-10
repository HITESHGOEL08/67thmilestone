from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.

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

class Register():
    name = models.CharField(max_length=100, default="")
    email = models.EmailField(max_length=100, unique=True)
    phone = models.BigIntegerField(unique=True)
    college_name = models.CharField(max_length=100)
    choice = (("M","Male"),("F","Female"),("O","Other"))
    gender = models.CharField(max_length=6,choices=choice)
    image = models.ImageField(upload_to='profile_images', blank=True)
    class Meta:
        verbose_name_plural = "Register"
    def __str__(self):
        return self.name
