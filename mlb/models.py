from django.db import models
from django.contrib.auth.models import User

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

	def __str__(self):
		"""Return a string representation of the model."""
		return self.name
