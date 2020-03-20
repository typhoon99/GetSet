from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    year=models.CharField(max_length=10)
    division=models.CharField(max_length=1)
    rollno=models.IntegerField()
    mobileno=models.IntegerField(primary_key=True)
    cgpa=models.IntegerField(default=0) 
    bio=models.CharField(max_length=200,default="NotFilled")
    isTeamLeader=models.BooleanField(default=False)
    post=models.CharField(max_length=10)
    isGroup=models.BooleanField(default=False)
    groupId=models.IntegerField(default=0)
    created_on=models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return str(self.firstName + " " +self.lastName)

class Students(models.Model):
    rno=models.IntegerField()
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    mobileNo=models.IntegerField(primary_key=True)

    def __str__(self):
        return str(str(self.rno)+"   "+self.firstName + " " +self.lastName)

class Guide(models.Model):
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    mobileNo=models.IntegerField(primary_key=True)

    def __str__(self):
        return str(self.firstName + " " +self.lastName)

class Topic(models.Model):
    topicName=models.CharField(max_length=30)
    domain=models.CharField(max_length=30)
    description=models.CharField(max_length=80)
    document=models.FileField(upload_to ='uploads/')
    created_on=models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.topicName


class ProjectGroup(models.Model):
    groupId=models.IntegerField(default=0,primary_key=True)
    user1=models.ForeignKey(UserProfile,on_delete=models.CASCADE, related_name = "member1")
    user2=models.ForeignKey(UserProfile,on_delete=models.CASCADE, related_name = "member2")
    user3=models.ForeignKey(UserProfile,on_delete=models.CASCADE, related_name = "member3")
    user4=models.ForeignKey(UserProfile,on_delete=models.CASCADE, related_name = "member4")
    guide=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    created_on=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.groupId
    
class Report(models.Model):
    report=models.FileField(upload_to ='reports/')
    description=models.TextField(blank=True)
    groupId=models.ForeignKey(ProjectGroup,on_delete=models.CASCADE)
    comment=models.TextField()
    created_on=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.groupId + " " +self.report)

class PPT(models.Model):   
    ppt=models.FileField(upload_to ='presentations/')
    description=models.TextField(blank=True)
    groupId=models.ForeignKey(ProjectGroup,on_delete=models.CASCADE)
    comment=models.TextField()
    created_on=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.groupId + " " +self.ppt)


