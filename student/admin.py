from django.contrib import admin
from .models import UserProfile,ProjectGroup,Student,Guide,Topic,Report,PPT

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(ProjectGroup)
admin.site.register(Student)
admin.site.register(Guide)
admin.site.register(Topic)
admin.site.register(Report)
admin.site.register(PPT)