from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from userena.forms import SignupForm


class SignupFormExtra(SignupForm):
    first_name = forms.CharField(max_length=50)
    middle_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=70, unique=True)
    mobile =forms.IntegerField(max_length=50)
    major= forms.CharField(max_length=50)
    interests = forms.TextField(widget=forms.Textarea)
    cv= forms.FileField(upload_to='CVs')

    # def __init__(self, *args, **kw):
    #     """
    #
    #     A bit of hackery to get the first name and last name at the top of the
    #     form instead at the end.
    #
    #     """
    #     super(SignupFormExtra, self).__init__(*args, **kw)
    #     # Put the first and last name at the top
    #     new_order = self.fields.keyOrder[:-2]
    #     new_order.insert(0, 'first_name')
    #     new_order.insert(1, 'last_name')
    #     self.fields.keyOrder = new_order

    def save(self):
        # First save the parent form and get the user.
        new_user = super(SignupFormExtra, self).save()

        # Get the profile, the `save` method above creates a profile for each
        # user because it calls the manager method `create_user`.
        # See: https://github.com/bread-and-pepper/django-userena/blob/master/userena/managers.py#L65
        user_profile = new_user.get_profile()

        user_profile.first_name = self.cleaned_data['first_name']
        user_profile.middle_name= self.cleaned_data['middle_name']
        user_profile.last_name = self.cleaned_data['last_name']
        user_profile.email=self.cleaned_data['email']
        user_profile.mobile=self.cleaned_data['mobile']
        user_profile.major=self.cleaned_data['major']
        user_profile.interests=self.cleaned_data['interests']
        user_profile.cv=self.cv





        #fill the remaining
        user_profile.save()

        # Userena expects to get the new user from this form, so return the new
        # user.
        return new_user