
from django.contrib import admin
from django.urls import path, include
from .views import show_bloghome
from loginreg import views
from userprofile import views


urlpatterns = [
	path( '', show_bloghome, name= 'blog'),
	path( 'profile/', views.profile, name= 'profile'),
	path( 'show_userprofile/', views.show_userprofile, name="showpro")
	
]
