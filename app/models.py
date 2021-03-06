from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
#from userena.models import UserenaBaseProfile

#class userena.models.UserenaSignup():
   #def activation_key_expired():
       #if True:
          # return activation_key
       #else:
           #False

class Organization(models.Model):
    organization = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField(max_length=70, unique=True)
    mobile = models.IntegerField(max_length=50)
    user = models.ManyToManyField(User)

class Event(models.Model):
    title= models.CharField(max_length=100)
    description = models.TextField()
    #date= models.DateField()
    time= models.DateTimeField()
    organization= models.ForeignKey(Organization)

class Registration(models.Model):
    event = models.ForeignKey(Event)
    user = models.ForeignKey(User)
    extra_info = models.TextField()