# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlb', '0008_auto_20171024_0426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='image'),
        ),
    ]
