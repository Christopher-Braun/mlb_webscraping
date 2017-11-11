from django.forms import ModelForm
from mlb.models import Picture, Project
from django import forms

class PictureForm(forms.ModelForm):
	class Meta:
		model = Picture
		fields = ('name', 'image')

class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ('name', 'description', 'file', 'calculations', 'proj_image')
