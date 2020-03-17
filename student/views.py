from django.shortcuts import render, redirect
from django import forms
from .forms import SignUpForm
from django.contrib.auth import login, authenticate

# Create your views here.
def login(request):
	return render(request, 'student/login.html', {})

def signup(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			email=form.cleaned_data.get('email')
			user = authenticate(username = username, password = raw_password)
			firstName=form.cleaned_data.get('firstName')
			lastName=form.cleaned_data.get('lastName')
			rollno=form.cleaned_data.get('rollNo')
			year=form.cleaned_data.get('year')
			division=form.cleaned_data.get('division')
			login(request, user)
			return redirect('ungrouped')
	else:
		form = SignUpForm()
	return render(request, 'student/signup.html', {'form':form})
