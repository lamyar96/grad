from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from app.models import Profile
from userena.forms import SignupForm
class SignUp(SignupForm):
    first_name = forms.CharField(max_length=50)
     middle_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=70, unique=True)
    mobile =forms.IntegerField(max_length=50)
    major= forms.CharField(max_length=50)
    interests = forms.TextField(widget=forms.Textarea)
    cv= forms.FileField(upload_to='CVs')