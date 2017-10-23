"""Defines URL patterns for mlb."""

from django.conf.urls import url

from . import views
app_name = 'mlb'

urlpatterns = [
	# Home page
	url(r'^$', views.index, name='index'),

	# Player page
	url(r'^players/$', views.players, name='players'),

	# Team page
	url(r'^teams/$', views.teams, name='teams'),

	# Individual team page
	url(r'^team/(?P<team_name>[a-z]+)/$', views.team, name='team'),

	]