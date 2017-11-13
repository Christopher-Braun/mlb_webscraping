from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save

class Team(models.Model):
	"""MLB Baseball Team"""
	name = models.CharField(max_length=4)
	full_name = models.CharField(max_length=50)
	#owner = models.ForeignKey(User)

	def __str__(self):
		"""Return a string representation of the model."""
		return self.name

class Player(models.Model):
	"""MLB Baseball Player"""
	name = models.CharField(max_length=100)
	position = models.CharField(max_length=10)
	league = models.CharField(max_length=5)
	games = models.CharField(max_length=10)
	Tav = models.CharField(max_length=7)
	VORP = models.CharField(max_length=7)
	FRAA = models.CharField(max_length=7)
	BWARP = models.CharField(max_length=7)
	team = models.ForeignKey(Team)
	date_modified = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""Return a string representation of the model."""
		return self.name

class Picture(models.Model):
    name = models.CharField(max_length=30)
    image = models.FileField(upload_to="static", blank = True, null = True)

    def __str__(self):
        return self.name

class Project(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=300)
	file = models.FileField(upload_to="static", blank = True, null = True)
	calculations = models.FileField(upload_to="static", blank = True, null = True)
	proj_image = models.FileField(upload_to="media", blank = True, null = True)
	
	def __str__(self):
		return self.name

class ProjectPic(models.Model):
	name = models.CharField(max_length=50)
	chart = models.FileField(upload_to="media", blank = True, null = True)
	project = models.ForeignKey(Project)