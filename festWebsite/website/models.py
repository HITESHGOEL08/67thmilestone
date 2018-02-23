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