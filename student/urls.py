from django.urls import path
from . import views
 
urlpatterns = [
	path('', views.home, name="home"),
	path('signup/', views.signup, name="signup"),
	path('createProfile/', views.createProfile, name="createProfile"),
	path('createGroup/', views.createGroup, name="createGroup"),
]
