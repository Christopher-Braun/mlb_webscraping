# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 09:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mlb', '0006_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='website',
        ),
    ]