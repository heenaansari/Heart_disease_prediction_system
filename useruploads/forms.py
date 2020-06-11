from django import forms

from .models import UserDocUpload

class UserDocUploadForm(forms.ModelForm):
	class Meta:
		model = UserDocUpload
		fields = ('docname', 'patientname', 'doctor', 'pdf')