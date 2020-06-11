from django.shortcuts import render

# Create your views here.

def show_indexhome(request):
	
	return render(request, 'indexhome.html', {})