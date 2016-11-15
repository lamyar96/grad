from django import forms
from app import models
from django.forms import ModelForm
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
