from django.shortcuts import render, redirect
from django import forms
from .forms import SignUpForm, ProfileForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from .models import UserProfile, Student
from django.contrib.auth.decorators import login_required
# from django.db import connection

# Create your views here.

def home(request):
    if request.POST.get('student'):
        return redirect('student/signUp')
    elif request.POST.get('guide'):
        return redirect('guide/signUp')
    else:
        return render(request,'student/home.html')
    
def studentSignUp(request):
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
            return redirect('createProfile')
    else:
        form=SignUpForm()
    return render(request,'student/signup.html', {'form':form})  #for form.as_p in .html 

def guideSignUp(request):
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
            return redirect('createProfile')
    else:
        form=SignUpForm()
    return render(request,'student/signup.html', {'form':form})  #for form.as_p in .html 

def createProfile(request):
    if request.method == "POST":
        userProfile=UserProfile()
        rollno=request.POST.get('rollno')
        division=request.POST.get('division')
        firstName=request.POST.get('firstName')
        lastName=request.POST.get('lastName')
        year=request.POST.get('year')
        mobileno=request.POST.get('mobileno')
        cgpa=request.POST.get('cgpa')
        bio=request.POST.get('bio')

        userProfile.user = request.user
        userProfile.userProfile=userProfile
        userProfile.rollNo=rollno
        userProfile.division=division
        userProfile.firstName=firstName
        userProfile.lastName=lastName
        userProfile.year=year
        userProfile.mobileNo=mobileno
        userProfile.cgpa=cgpa
        userProfile.bio=bio

        student = Student.objects.get(rollNo=rollno)
        print(userProfile.firstName)
        fields = {'firstName':'match','lastName':'match','mobileNo':'match'}

        if(str(student.mobileNo) != mobileno):
            fields['mobileNo']='unmatch'
        if(str(student.firstName) != firstName):
            fields['firstName']='unmatch'
        if(str(student.lastName) != lastName):
            fields['lastName']='unmatch'
        print('matching done')
        print(fields['firstName'])
        print(fields['lastName'])
        print(fields['mobileNo'])
        if(fields['firstName']=='match' and fields['lastName']=='match' and fields['mobileNo']=='match'):
            userProfile.save()
            print('saved')
        return render(request,'student/createGroup.html',fields)
    else:
        return render(request,'student/ProfileForm.html')

def createGroup(request):
    fields={}
    userProfile=UserProfile()
    for firstName in userProfile.firstName:
        if(userProfile.isGroup==False):
            fields.append('userProfile.firstName')
        endif
    
    return render(request,'student/createGroup.html',fields)


# def Test(request,form):
#     return render(request,'student/Test.html', {'form':form})