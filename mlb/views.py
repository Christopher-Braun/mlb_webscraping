from django.shortcuts import render, render_to_response, redirect
from bs4 import BeautifulSoup
import urllib.request
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext, Template
from datetime import datetime, timedelta
import requests

from mlb.models import Team, Player, Picture, Project, ProjectPic
from mlb.forms import PictureForm, ProjectForm





def index(request):
	"""The home page for MLB"""

	wiki = "http://legacy.baseballprospectus.com/standings/index.php?dispgroup=all&submit=Go"
	page = urllib.request.urlopen(wiki)
	soup = BeautifulSoup(page, 'lxml')

	teams, name = [], []
	for row in soup.find_all('option'):
		if row not in teams:
			teams.append(row.get('value'))
			team_name = row.get('value')
			name.append(row.get_text())
			full_name = row.get_text()
			try:
				team = Team.objects.get(name = team_name)
			except Team.DoesNotExist:
				team = None
				if team is None:
					team = Team(name=team_name, full_name=full_name)
					team.save()


	context = {'teams': teams, 'name': name, 'team': team}

	return render(request, 'mlb/index.html', context)


def players(request):

	wiki1 = "http://legacy.baseballprospectus.com/sortable/index.php?cid=1918873"
	page1 = urllib.request.urlopen(wiki1)
	soup1 = BeautifulSoup(page1, 'lxml')

	players = []
	for element in soup1.find_all('tr')[6:1330]:
		players.append(element.a.get_text())
		try:
			player = Player.objects.get(name = element.a.get_text())
			player.league = element.contents[3].get_text()
			player.games = element.contents[6].get_text()
			player.Tav = element.contents[34].get_text()
			player.VORP = element.contents[35].get_text()
			player.FRAA = element.contents[36].get_text()
			player.BWARP = element.contents[37].get_text()
			player.save()
		except Player.DoesNotExist:
			player = None
			if player is None:
				player = Player(name = element.a.get_text(),
				league = element.contents[3].get_text(),
				games = element.contents[6].get_text(),
				Tav = element.contents[34].get_text(),
				VORP = element.contents[35].get_text(),
				FRAA = element.contents[36].get_text(),
				BWARP = element.contents[37].get_text())
				tm = Team.objects.get(name = element.contents[2].get_text().lower())
				player.team = tm
				player.save()

	player_new = Player.objects.all()

	context = {'players': players, 'player_new': player_new}

	return render(request, 'mlb/players.html', context)



@login_required
def team(request, team_name):
	team = Team.objects.get(name = team_name)
	players = team.player_set.all()

	# Make sure the team belongs to the current user.
	#if team.owner != request.user:
	#	raise Http404

	context = {'players': players, 'team': team}

	return render(request, 'mlb/team.html', context)

@login_required
def teams(request):
	teams = Team.objects.all()

	context = {'teams': teams}

	return render(request, 'mlb/teams.html', context)

@login_required
def pictures(request):
	pictures = Picture.objects.all()

	context = {'pictures': pictures}
	
	return render(request, 'mlb/pictures.html', context)

@login_required
def picture(request, picture_id):
	picture = Picture.objects.get(id = picture_id)
	
	# Make sure the team belongs to the current user.
	#if team.owner != request.user:
	#	raise Http404

	context = {'picture': picture}

	return render(request, 'mlb/picture.html', context)

@login_required
def add_picture(request):
	"""Add a new picture."""
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = PictureForm()
	else:
		# POST data submitted; process data.
		form = PictureForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('mlb:pictures'))

	context = {'form': form}
	return render(request,'mlb/add_picture.html', context)

@login_required
def projects(request):
	"""Display Projects"""
	projects = Project.objects.all()

	context = {'projects': projects}
	
	return render(request, 'mlb/projects.html', context)

@login_required
def project(request, project_name):
	project = Project.objects.get(name = project_name)
	pro_file = str(project.file)
	pro_calc = str(project.calculations)
	with open(pro_file) as file_object:
		lines = file_object.readlines()
	file_object.close()

	if pro_calc:
		with open(pro_calc) as file_object:
			calcs = file_object.readlines()
		file_object.close()
	else:
		nocalcs = '/Users/mrcrb/Documents/Python/Baseball/ll_env/static/nocalcs.txt'
		with open(nocalcs) as file_object:
			calcs = file_object.readlines()
		file_object.close()

	charts = project.projectpic_set.all()
	

	# Make sure the team belongs to the current user.
	#if team.owner != request.user:
	#	raise Http404

	context = {'project': project, 'lines': lines, 'calcs': calcs, 'charts': charts}

	return render(request, 'mlb/project.html', context)
	
@login_required
def add_project(request):
	"""Add a new project."""
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = ProjectForm()
	else:
		# POST data submitted; process data.
		form = ProjectForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('mlb:projects'))

	context = {'form': form}
	return render(request,'mlb/add_project.html', context)


"""def add_picture(request):
	name = Picture.objects.get('name')
	if request.method == 'GET':
		form = PictureForm()
	else:
		name = Picture.objects.get(name = name)
		form = ProductForm(request.POST, request.FILES)
		p = Picture(name = request.POST.get('name'), website = request.POST.get('website'), image = request.FILES['image'])
		print("image", p.picture)
		p.save()

		return redirect('/mlb/teams/')
	return render(request, 'add_picture.html', {'form':form, 'name': name})
	
	
def players(request):
	time_threshold = datetime.now() - timedelta(days=14)
	player_old = Player.objects.filter(date_modified__lt = time_threshold)
	if not player_old:
		wiki1 = "http://legacy.baseballprospectus.com/sortable/index.php?cid=1918873"
		page1 = urllib.request.urlopen(wiki1)
		soup1 = BeautifulSoup(page1, 'lxml')

		players = []
		for element in soup1.find_all('tr')[6:1330]:
			players.append(element.a.get_text())
			try:
				player = Player.objects.get(name = element.a.get_text())
				player.league = element.contents[3].get_text()
				player.games = element.contents[6].get_text()
				player.Tav = element.contents[34].get_text()
				player.VORP = element.contents[35].get_text()
				player.FRAA = element.contents[36].get_text()
				player.BWARP = element.contents[37].get_text()
				player.save()
			except Player.DoesNotExist:
				player = None
				if player is None:
					player = Player(name = element.a.get_text(),
					league = element.contents[3].get_text(),
					games = element.contents[6].get_text(),
					Tav = element.contents[34].get_text(),
					VORP = element.contents[35].get_text(),
					FRAA = element.contents[36].get_text(),
					BWARP = element.contents[37].get_text())
					tm = Team.objects.get(name = element.contents[2].get_text().lower())
					player.team = tm
					player.save()

		player_new = Player.objects.all()

	context = {'players': players, 'player_new': player_new}

	return render(request, 'mlb/players.html', context)"""