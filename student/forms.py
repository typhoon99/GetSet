from .models import UserProfile, Students, Guide, Topic, ProjectGroup, Report, PPT
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUp(forms.Form):
    username = forms.CharField(label='username')
    email = forms.EmailField(label='email')
    password1 = forms.CharField(label='password1')
    password2 = forms.CharField(label='password2')
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2',]