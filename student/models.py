from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    firstName = models.CharField(max_length = 50)
    lastName = models.CharField(max_length = 50)
    year = models.CharField(max_length = 10)
    division = models.CharField(max_length = 1)
    rollNo = models.IntegerField()
    mobileNo = models.IntegerField(primary_key = True)
    cgpa = models.FloatField(default = 0.0)
    bio = models.TextField()
    isTeamLeader = models.BooleanField(default = False)
    post = models.CharField(max_length = 10)
    isGrouped = models.BooleanField(default = False)
    isAssigned = models.BooleanField(default = False)
    groupId = models.IntegerField(blank = True, null = True)
    createdOn = models.DateTimeField(auto_now_add = True)
    modifiedOn = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return str(self.firstName + " " + self.lastName)

    def modify(self):
        self.modifiedOn = timezone.now()
        self.save()

    def groupUser(self, gId):
        if self.post == 'Student':
            self.isGrouped = True
            self.isAssigned = True
            self.groupId = gId
            self.save()
    
    def assignGuide(self, gId):
        if self.post == 'Guide':
            self.isGrouped = False
            self.isAssigned = True
            self.groupId = gId
            self.save()

    def makeTeamLeader(self):
        if self.post == 'Student':
            self.isTeamLeader = True
            self.save()

class Student(models.Model):
    rollNo = models.IntegerField()
    firstName = models.CharField(max_length = 50)
    lastName = models.CharField(max_length = 50)
    mobileNo = models.IntegerField(primary_key = True)

    def __str__(self):
        return str(str(self.rollNo) + "   " + self.firstName + " " + self.lastName)

class Guide(models.Model):
    firstName = models.CharField(max_length = 50)
    lastName = models.CharField(max_length = 50)
    mobileNo = models.IntegerField(primary_key = True)

    def __str__(self):
        return str(self.firstName + " " + self.lastName)

class Topic(models.Model):
    topicName = models.CharField(max_length = 30)
    domain = models.CharField(max_length = 30)
    description = models.TextField()
    document = models.FileField(upload_to = 'topics')
    createdOn = models.DateTimeField(auto_now_add = True)
    isTaken = models.BooleanField(default = False)
   
    def __str__(self):
        return self.topicName

    def take(self):
        self.isTaken = True
        self.save()

class ProjectGroup(models.Model): 
    #groupId = models.IntegerField(default = 0, primary_key = True)
    user1 = models.ForeignKey(UserProfile, on_delete = models.CASCADE, related_name = "member1", blank = False, null = False)
    user2 = models.ForeignKey(UserProfile, on_delete = models.CASCADE, related_name = "member2")
    user3 = models.ForeignKey(UserProfile, on_delete = models.CASCADE, related_name = "member3")
    user4 = models.ForeignKey(UserProfile, on_delete = models.CASCADE, related_name = "member4")
    guide = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE, blank = True, null = True)
    createdOn = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.groupId

class Report(models.Model):
    report = models.FileField(upload_to = 'reports')
    description = models.TextField(blank = True)
    groupId = models.ForeignKey(ProjectGroup, on_delete = models.CASCADE)
    comment = models.TextField()
    modifiedOn = models.DateTimeField(default = timezone.now)
    lastModifiedBy = models.ForeignKey(UserProfile, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return str(self.groupId + " " + self.report)

    def modify(self, user):
        self.modifiedOn = timezone.now()
        self.lastModifiedBy = user
        self.save()

class PPT(models.Model):
    ppt = models.FileField(upload_to = 'presentations')
    description = models.TextField(blank = True)
    groupId = models.ForeignKey(ProjectGroup, on_delete = models.CASCADE)
    comment = models.TextField()
    modifiedOn = models.DateTimeField(default = timezone.now)
    lastModifiedBy = models.ForeignKey(UserProfile, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return str(self.groupId + " " + self.ppt)

    def modify(self, user):
        self.modifiedOn = timezone.now()
        self.lastModifiedBy = user
        self.save()