from django.shortcuts import render, redirect
from django import forms
from .forms import SignUpForm, ProfileForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from .models import UserProfile,Students

# Create your views here.
def signup(request):
    if request.method == "POST":     #built-in request.method
        form=SignUpForm(request.POST)    #assign values as in constructor
        if form.is_valid():
            print('valid')
            form.save()
            print('saved')
            username=form.cleaned_data.get('username')  #cleaned_data removes extraw char added by server.
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=username, password=raw_password)
            login(request,user)  #make user login of requested user
            return redirect('login')
    else:
        form=SignUpForm()
    return render(request,'student/signup.html', {'form':form})  #for form.as_p in .html 

def ProfileForm(request):
    if request.method == "POST":
        userProfile=UserProfile()
        userProfile.rollno=request.POST.get('rollno')
        userProfile.division=request.POST.get('division')
        userProfile.firstName=request.POST.get('firstName')
        userProfile.lastName=request.POST.get('lastName')
        userProfile.year=request.POST.get('year')
        userProfile.mobileno=request.POST.get('mobileno')
        userProfile.cgpa=request.POST.get('cgpa')
        userProfile.bio=request.POST.get('bio')

        student = Students.objects.get(rno=userProfile.rollno)
        fields = {'firstName':'match','lastName':'match','mobileNo':'match'}

        if(student.mobileNo != userProfile.mobileno):
            fields['mobileNo']='unmatch'
        if(student.firstName != userProfile.firstName):
            fields['firstName']='unmatch'
        if(student.lastName != userProfile.lastName):
            fields['lastName']='unmatch'
        if(fields['firstName']=='match' and fields['lastName']=='match' and fields['mobileName']=='match'):
            userProfile.save()
        return render(request,'student/ProfileForm.html',fields)
    else:
        return render(request,'student/ProfileForm.html')
        
# def Test(request,form):
#     return render(request,'student/Test.html', {'form':form})