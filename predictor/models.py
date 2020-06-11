from django.db import models

# Create your models here.
class Prediction(models.Model):
	pid = models.AutoField(primary_key=True)
	pname = models.CharField(max_length=255)
	page = models.DecimalField(decimal_places=0, max_digits=2)
	pgender = models.DecimalField(decimal_places=0, max_digits=2)
	pcp = models.DecimalField(decimal_places=0, max_digits=2)
	ptrestbps = models.CharField(max_length=5)
	pchol = models.CharField(max_length=5)
	pfbs = models.DecimalField(decimal_places=0, max_digits=2)
	prestecg = models.DecimalField(decimal_places=0, max_digits=2)
	pthalach = models.CharField(max_length=5)
	pexang = models.DecimalField(decimal_places=0, max_digits=2)
	poldpeak = models.CharField(max_length=5)
	pslope = models.DecimalField(decimal_places=0, max_digits=2)
	pca = models.CharField(max_length=5)
	pthal = models.IntegerField()
	presult = models.CharField(max_length=255)