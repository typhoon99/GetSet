from .models import UserProfile, Students, Guide, Topic, ProjectGroup, Report, PPT
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    mobileno = forms.IntegerField()
    
    class Meta:
        model = User, UserProfile
        fields = ['rollno','firstName','lastName','year','division','mobileno','username','password1','password2',]
