from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .forms import SignUpForm, ProfileForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from .models import UserProfile, Student, User, ProjectGroup
from django.contrib.auth.decorators import login_required
# from django.db import connection

# Create your views here.

def loginUser(request):
    if request.POST.get('studentLogin'):
        return redirect('studentLogin')
    elif request.POST.get('guideLogin'):
        return redirect('guideLogin')
    else:
        return render(request,'student/loginUser.html')


def LogoutView(request):
    return render(request,'home')

def studentLogin(request,pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'student/studentLogin.html',{'user':user})

def guideLogin(request):
    return render(request,'Guide/guideLogin.html')

def studentValidate(request,pk):
    if request.method == "POST":
        UserName=request.POST.get('userName')
        Password=request.POST.get('password')
        user=authenticate(username=UserName,password=Password)
        student= User.objects.get(username=UserName).pk
        User1=get_object_or_404(UserProfile,pk=student)
        #print(User1)
        #print(student)
        if user is not None:
            #student= UserProfile.objects.get(user=UserName)
            if User1:
               return redirect('createGroup')
            else:
                return redirect('studentCreateProfile')
        else:
            return redirect('studentLogin')
    else:
        return render(request,"student/studentLogin.html")

def guideValidate(request):
    if request.method == "POST":
        UserName=request.POST.get('userName')
        Password=request.POST.get('password')
        user=authenticate(username=UserName,password=Password)
        if user is not None:
            return redirect('guideCreateProfile')
        else:
            return redirect('guideLogin')
    else:
        return render(request,"guide/guideLogin.html")

def home(request):
    if request.POST.get('student'):
        return redirect('student/signUp')
    elif request.POST.get('guide'):
        return redirect('guide/signUp')
    #elif request.POST.get('loginUser'):
    #    return redirect('loginUser')
    else:
        return render(request,"student/home.html")
    
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
            return redirect('studentCreateProfile')
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
            return redirect('guideCreateProfile')
    else:
        form=SignUpForm()
    return render(request,'guide/guideSignUp.html', {'form':form})  #for form.as_p in .html 

@login_required
def studentCreateProfile(request):
    if request.method == "POST":
        rollno=request.POST.get('rollno')
        firstName=request.POST.get('firstName')
        lastName=request.POST.get('lastName')
        year=request.POST.get('year')
        division=request.POST.get('division')
        mobileno=request.POST.get('mobileno')
        cgpa=request.POST.get('cgpa')
        bio=request.POST.get('bio')

        student = Student.objects.get(rollNo=rollno)
        print(student.firstName)
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
            userProfile=UserProfile()
            userProfile.user = request.user
            userProfile.rollNo=rollno
            userProfile.division=division
            userProfile.firstName=firstName
            userProfile.lastName=lastName
            userProfile.year=year
            userProfile.mobileNo=mobileno
            userProfile.cgpa=cgpa
            userProfile.bio=bio
            userProfile.post='Student'
            userProfile.modify()
            userProfile.save()
            print('saved')
            return redirect('createGroup')
        else:
            return redirect('createGroup')

    else:
        return render(request,'student/studentCreateProfile.html')

@login_required
def guideCreateProfile(request):
    if request.method == "POST":
        firstName=request.POST.get('firstName')
        lastName=request.POST.get('lastName')
        mobileNo=request.POST.get('mobileno')
        bio=request.POST.get('bio')
        guide = Guide.objects.get(mobileNo=mobileNo)
        print(userProfile.firstName)
        fields = {'firstName':'match','lastName':'match','mobileNo':'match'}

        if(str(guide.mobileNo) != mobileno):
            fields['mobileNo']='unmatch'
        if(str(guide.firstName) != firstName):
            fields['firstName']='unmatch'
        if(str(guide.lastName) != lastName):
            fields['lastName']='unmatch'
        print('matching done')
        print(fields['firstName'])
        print(fields['lastName'])
        print(fields['mobileNo'])
        if(fields['firstName']=='match' and fields['lastName']=='match' and fields['mobileNo']=='match'):
            userProfile=UserProfile()
            userProfile.user = request.user
            userProfile.userProfile=userProfile
            userProfile.firstName=firstName
            userProfile.lastName=lastName
            userProfile.mobileNo=mobileno
            userProfile.bio=bio
            userProfile.post='Guide'
            userProfile.modify()
            userProfile.save()
            print('saved')
            return render(request,'student/createGroup.html',fields)
    else:
        return render(request,'student/createProfile.html')


def createGroup(request):
    students = UserProfile.objects.filter(isGrouped=False).order_by("rollNo")
    return render(request,'student/createGroup.html',{'students':students})

def registerGroup(request):
    if request.method == "POST":
        selected = request.POST.getlist("checks[]")
        #for i in selected:
        #list = str.split (",")
        #print ("list: ", list)
        #print(selected[0])
        #print(selected[1])
        #print(selected[0])
        #print(request.POST)
        #userProfile=UserProfile()
        projectGroup=ProjectGroup()
        userProfile=UserProfile()
        student1 = UserProfile.objects.get(rollNo=int(selected[0]))
        projectGroup.user1=student1
        student2 = UserProfile.objects.get(rollNo=int(selected[1]))
        projectGroup.user2=student2
        student3 = UserProfile.objects.get(rollNo=int(selected[2]))
        projectGroup.user3=student3
        student4 = UserProfile.objects.get(rollNo=int(selected[3]))
        projectGroup.user4=student4
        #projectGroup.modify()
        projectGroup.save()
        return redirect("yourTopic")
    else:
        return render(request,'student/yourTopic.html')


# @login_required
# def createGroup(request):
#     fields={}
#     userProfile=UserProfile()
#     for firstName in userProfile.firstName:
#         if(userProfile.isGroup==False):
#             fields.append('userProfile.firstName')
#     return render(request,'student/createGroup.html',fields)

# def Test(request,form):
#     return render(request,'student/Test.html', {'form':form})