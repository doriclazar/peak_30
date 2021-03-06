# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-16 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20180716_0723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='botprofile',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='groupprofile',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='icon',
        ),
        migrations.AddField(
            model_name='botprofile',
            name='icone',
            field=models.CharField(default='fas fa-android', max_length=64),
        ),
        migrations.AddField(
            model_name='groupprofile',
            name='icone',
            field=models.CharField(default='fas fa-users', max_length=64),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='icone',
            field=models.CharField(default='fas fa-user', max_length=64),
        ),
    ]
