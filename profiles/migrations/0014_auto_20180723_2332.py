# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-23 23:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_auto_20180716_0734'),
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
    ]
