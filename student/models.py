from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    year=models.CharField(max_length=10)
    division=models.CharField(max_length=1)
    rollno=models.IntegerField()
    mobileno=models.IntegerField(primary_key=True) 
    isTeamLeader=models.BooleanField(default=False)
    post=models.CharField(max_length=10)
    isGroup=models.BooleanField(default=False)
    cgpa=models.FloatField()
    bio=models.TextField()
    image=models.ImageField(upload_to='images/')
    groupid=models.IntegerField()
    created_on=models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return str(self.firstname + " " +self.lastname)

class Students(models.Model):
    rno=models.IntegerField()
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    mobileno=models.IntegerField(primary_key=True)

    def __str__(self):
        return str(self.firstname + " " +self.lastname)

class Guide(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    mobileno=models.IntegerField(primary_key=True)

    def __str__(self):
        return str(self.firstname + " " +self.lastname)

class Topic(models.Model):
    topicName=models.CharField(max_length=30)
    domain=models.CharField(max_length=30)
    description=models.CharField(max_length=80)
    document=models.FileField(upload_to ='uploads/')
    created_on=models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.topicName


class Group(models.Model):
    groupid=models.IntegerField(primary_key=True)
    user1=models.ForeignKey(UserProfile,on_delete=models.CASCADE, related_name = "member1")
    user2=models.ForeignKey(UserProfile,on_delete=models.CASCADE, related_name = "member2")
    user3=models.ForeignKey(UserProfile,on_delete=models.CASCADE, related_name = "member3")
    user4=models.ForeignKey(UserProfile,on_delete=models.CASCADE, related_name = "member4")
    guide=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    created_on=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.groupid
    
class Report(models.Model):
    report=models.FileField(upload_to ='reports/')
    description=models.TextField(blank=True)
    groupid=models.ForeignKey(Group,on_delete=models.CASCADE)
    comment=models.TextField()

    def __str__(self):
        return str(self.groupid + " " +self.report)

class PPT(models.Model):   
    ppt=models.FileField(upload_to ='presentations/')
    description=models.TextField(blank=True)
    groupid=models.ForeignKey(Group,on_delete=models.CASCADE)
    comment=models.TextField()

    def __str__(self):
        return str(self.groupid + " " +self.ppt)


