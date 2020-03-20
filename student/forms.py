from .models import UserProfile, Students, Guide, Topic, ProjectGroup, Report, PPT
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email=forms.EmailField(max_length=200,help_text="Enter your official email")
    
    class Meta:
        model= User
        fields = ['username','email','password1','password2',]

class ProfileForm(forms.ModelForm):
        
    class Meta:
        model= UserProfile
        fields = ['rollno','firstName','lastName','year','division','mobileno','cgpa','bio']
    
    