from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
# from userena.models import UserenaBaseProfile

#class MyProfile(UserenaBaseProfile):
    #user = models.OneToOneField(User,
                                #unique=True,
                                #verbose_name=_('user'),
                               # related_name='my_profile')
    #favourite_snack = models.CharField(_('favourite snack'),
                                    #   max_length=5)
class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, null=True, blank=True, unique=True)
    mobile = models.IntegerField(max_length=50)
    major= models.CharField(max_length=50)
    interests = models.TextField()
    cv= models.FileField(upload_to='CVs')
    user= models.OneToOneField(User)

    def __unicode__(self):
        return self.first_name

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

class Registration(models.Model):
    event = models.ForeignKey(Event)
    user = models.ForeignKey(User)