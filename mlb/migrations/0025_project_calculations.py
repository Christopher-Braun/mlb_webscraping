# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 01:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlb', '0024_auto_20171108_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='calculations',
            field=models.FileField(blank=True, null=True, upload_to='static'),
        ),
    ]