from django.contrib import admin
from .models import Doctor, Category, Blog
# Register your models here.

admin.site.register(Doctor)
admin.site.register(Category)
admin.site.register(Blog)