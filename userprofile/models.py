from django.db import models

# Create your models here.
class UserProfile(models.Model):
	username = models.CharField(max_length=100)
	dob =models.DateField()
	genetic_history = models.TextField()
	medical_history = models.TextField()


	def __str__(self):
		return self.username
