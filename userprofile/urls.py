

from django.contrib import admin
from django.urls import path, include
from .views import show_userprofile, update_userprofile, profile
urlpatterns = [
	path( '', profile, name='profile'),
	path( 'show_userprofile/', show_userprofile, name='showpro'),
	path( 'show_userprofile/updateuserprofile', update_userprofile, name='update_userprofile'),
	#path( 'show_userprofile/profile', show_userprofile, name='show_userprofile'),

	path('updateuserprofile/', update_userprofile, name='update_userprofile')
	
]
