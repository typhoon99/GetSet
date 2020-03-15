from django.db import models
from django.contrib.auth.models import User
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

    def __str__(self):
        return str(self.firstname + " " +self.lastname)

