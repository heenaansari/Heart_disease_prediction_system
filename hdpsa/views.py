from django.shortcuts import render
from .models import Blog
# Create your views here.
def show_bloghome(request):
	blog_list = Blog.objects.all()
	context = {'blog_list' : blog_list }
	return render(request, 'bloghome.html', context)
