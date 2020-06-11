from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def login(request):
	if request.method== 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			value = 'User does not exist'
			return render(request,'404.html',{'contextlogin': value})

	else:
		return render(request, 'login.html', {})


def signin(request):
	return render(request, 'register.html',{})




def register(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		email = request.POST['email']

		if password1==password2:
			if User.objects.filter(username=username).exists():
				value = 'User name already taken'
				return render(request,'404.html',{'context': value})
							
			elif User.objects.filter(email=email).exists():
				value = 'Email already taken'
				return render(request,'404.html',{'context': value})
				
			else:
				user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
				user.save()
				print('User Registered')

		else:
			value = 'Password does not matches'
			return render(request,'404.html',{'context': value})
		return render(request, 'login.html',{})
	else:
		return render(request, 'register.html',{})


@login_required(login_url='/signin/login/')
def profile(request):
	return render(request, 'profile.html', {})

