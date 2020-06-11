
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from django.conf.urls.static import static

from .views import register, profile, signin, login
from userprofile import views


urlpatterns = [
	path( '',signin, name= "signin"),
	path('register/', register, name="register"),
	#path('register/profile/', profile, name="profile"),
	path('login/',login, name='login'),
	path('login/loginsubmission/',login, name='login'),
	path('login/loginsubmission/profile', profile, name='profile'),
	path('register/loginsubmission/',login,name='login')
	#path('submitregister/', submitreg, name="submit"),
	#path('submitregister/profile/', profile, name="profile"),

]




