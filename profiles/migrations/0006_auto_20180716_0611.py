# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-16 06:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20180716_0244'),
    ]

    operations = [
        migrations.AddField(
            model_name='botprofile',
            name='icon',
            field=models.CharField(default='fas fa-stroopwafel', max_length=16),
        ),
        migrations.AddField(
            model_name='groupprofile',
            name='icon',
            field=models.CharField(default='fas fa-stroopwafel', max_length=16),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='icon',
            field=models.CharField(default='fas fa-stroopwafel', max_length=16),
        ),
    ]
