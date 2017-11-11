# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlb', '0005_remove_team_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='image')),
                ('website', models.URLField()),
            ],
        ),
    ]
