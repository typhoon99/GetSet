from django.urls import path
from . import views
 
urlpatterns = [
	path('', views.loginUser, name="loginUser"),
	path('signup/', views.signup, name="signup"),
]
