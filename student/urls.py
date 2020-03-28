from django.urls import path
from . import views
 
urlpatterns = [
	path('', views.home, name="home"),
	# path('signup/', views.signup, name="signup"),
	path('createGroup/', views.createGroup, name="createGroup"),
	path('student/signUp/', views.studentSignUp, name="studentSignUp"),
	path('guide/signUp/', views.guideSignUp, name="guideSignUp"),
	path('loginUser/',views.loginUser,name="loginUser"),
	path('studentLogin/', views.studentLogin, name="studentLogin"),
	path('guideLogin/', views.guideLogin, name="guideLogin"),
	path('studentValidate/', views.studentValidate, name="studentValidate"),
	path('guideValidate/', views.guideValidate, name="guideValidate"),
	path('studentCreateProfile/', views.studentCreateProfile, name="studentCreateProfile"),
	path('guideCreateProfile/', views.guideCreateProfile, name="guideCreateProfile"),
	path('registerGroup/', views.registerGroup, name="registerGroup"),
]
