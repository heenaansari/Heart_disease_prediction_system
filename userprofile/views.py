from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import UserProfileForm
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .models import UserProfile
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='/signin/login/')
def show_userprofile(request):
	username = None
	if request.user.is_authenticated:
		username = request.user.username

	pros = UserProfile.objects.filter(username=username)
	return render(request, 'show_profile.html', {'pros': pros})

	
@login_required(login_url='/signin/login/')
def update_userprofile(request):
	if request.method == "POST":
		print("profile")
		form = UserProfileForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/profile/')
	else:
		form = UserProfileForm()

	return render(request, 'updateprofile.html', {'form': form})

@login_required(login_url='/signin/login/')
def profile(request):
	return render(request, 'profile.html', {})
