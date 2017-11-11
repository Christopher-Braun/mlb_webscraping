"""Defines URL patterns for mlb."""

from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

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

	# Pictures
	url(r'^pictures/$', views.pictures, name='pictures'),

	# Detail page for a single picture
	url(r'^pictures/(?P<picture_id>\d+)/$', views.picture, name='picture'),
	
	# Picture page
	url(r'^add_picture/$', views.add_picture, name='add_picture'),

	# Projects
	url(r'^projects/$', views.projects, name='projects'),

	# Detail page for a single project
	url(r'^project/(?P<project_name>[A-Za-z]+)/$', views.project, name='project'),

	# Project page
	url(r'^add_project/$', views.add_project, name='add_project'),

	] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)