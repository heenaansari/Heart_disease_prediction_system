from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import UserDocUploadForm
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .models import UserDocUpload
from django.contrib.auth.decorators import login_required


@login_required(login_url='/signin/login/')
def show_userdoc(request):
	username = None
	if request.user.is_authenticated:
		username = request.user.username
	print(username)
	docs = UserDocUpload.objects.filter(patientname=username)
	return render(request, 'show_userdoc.html', {'docs': docs})
	
def upload_userdoc(request):
	if request.method == "POST":
		form = UserDocUploadForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/show_userdoc/')
	else:
		form = UserDocUploadForm()

	return render(request, 'upload_userdoc.html', {'form': form})