# Workflow 2 -> admin.py for workflow 3
from django.contrib.auth.models import User
from django import forms
from learning.models import UserProfileInfo

class UserInfoForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_link','profile_pic')