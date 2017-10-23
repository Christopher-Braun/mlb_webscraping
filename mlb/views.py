from django.shortcuts import render
from bs4 import BeautifulSoup
import urllib.request
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from mlb.models import Team, Player

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


def teams(request):
	teams = Team.objects.all()

	context = {'teams': teams}

	return render(request, 'mlb/teams.html', context)