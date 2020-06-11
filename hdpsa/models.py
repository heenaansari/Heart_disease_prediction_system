from django.db import models

# Create your models here.
class Doctor(models.Model):
	did = models.AutoField(primary_key=True)
	dname = models.CharField(max_length=255)
	demail = models.EmailField(max_length=254)
	dcontact = models.CharField(max_length=10)
	dspeciality = models.CharField(max_length=255)

class Category(models.Model):
	cid = models.AutoField(primary_key=True)
	cname = models.CharField(max_length=255)
		

class Blog(models.Model):
	categories = models.ManyToManyField(Category, blank = True)
	bid = models.AutoField(primary_key=True)
	btitle = models.CharField(max_length=255)
	bauthor = models.CharField(max_length=255)
	bdate =  models.DateField()
	bdescription = models.CharField(max_length=255, default='')
	bcontent = models.TextField(default='')

