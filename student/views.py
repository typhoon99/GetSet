from django.shortcuts import render, redirect
from django import forms
from .forms import SignUp
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect

# Create your views here.
def login(request):
	return render(request, 'student/login.html', {})

def signup(request):
	if request.method == "POST":
		form = SignUp(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			email=form.cleaned_data.get('email')
			user = authenticate(username = username, password = raw_password)
			login(request,user)
			return HttpResponseRedirect('/ungrouped/')
	else:
		form = SignUp()
	return render(request, 'student/signup.html', {'form':form})
