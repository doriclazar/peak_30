# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-16 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_auto_20180716_0731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='botprofile',
            name='icon',
        ),
        migrations.AddField(
            model_name='botprofile',
            name='icone',
            field=models.CharField(default='fas fa-robot', max_length=64),
        ),
    ]
