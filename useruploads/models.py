from django.db import models

# Create your models here.
class UserDocUpload(models.Model):
	docname = models.CharField(max_length=100)
	patientname =models.CharField(max_length=100, default=" ")
	doctor = models.CharField(max_length=100)
	pdf = models.FileField(upload_to='userdocupload/pdfs/')


	def __str__(self):
		return self.docname
