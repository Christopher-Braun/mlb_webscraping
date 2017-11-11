"""Defines URL patterns for users"""

from django.conf.urls import url, include
from django.contrib.auth.views import login
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
	# Login page
	url(r'^login/$', login, {'template_name': 'users/login.html'},
			name='login'),

	# Logout page
	url(r'^logout/$', views.logout_view, name='logout'),

	# Registration page
	url(r'^register/$', views.register, name='register'),
]