# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-08 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlb', '0022_remove_project_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
