
from django.contrib import admin
from django.urls import path, include
from .views import show_userdoc, upload_userdoc
urlpatterns = [
	path( '', show_userdoc, name='doc'),
	path('upload/', upload_userdoc, name='upload')
	
]
