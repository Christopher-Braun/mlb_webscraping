# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 22:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mlb', '0004_team_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='owner',
        ),
    ]
