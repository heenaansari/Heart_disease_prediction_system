
from django.contrib import admin
from django.urls import path, include
from .views import show_indexhome

urlpatterns = [
	path( '', show_indexhome, name= 'healthhome'),
	
	
]
