from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from userena.models import UserenaBaseProfile

class Profile(UserenaBaseProfile):
    user = models.OneToOneField(User, unique=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    #email = models.EmailField(max_length=70, unique=True) already in django
    mobile = models.IntegerField(max_length=50)
    major= models.CharField(max_length=50)
    interests = models.TextField()
    cv= models.FileField(upload_to='CVs')
