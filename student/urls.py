from django.urls import path
from . import views
 
urlpatterns = [
	path('', views.home, name="home"),
	# path('signup/', views.signup, name="signup"),
	path('createGroup/', views.createGroup, name="createGroup"),
	path('student/signUp/', views.studentSignUp, name="studentSignUp"),
	path('guide/signUp/', views.guideSignUp, name="guideSignUp"),
	path('student/createProfile/', views.studentCreateProfile, name="studentCreateProfile"),
	path('guide/createProfile/', views.guideCreateProfile, name="guideCreateProfile"),
]
