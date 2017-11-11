from django.contrib import admin

from mlb.models import Team, Player, Picture, Project, ProjectPic

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Picture)
admin.site.register(Project)
admin.site.register(ProjectPic)