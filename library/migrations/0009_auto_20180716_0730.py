# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-16 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_auto_20180716_0728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='module',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='profession',
            name='icon',
        ),
        migrations.AddField(
            model_name='category',
            name='icone',
            field=models.CharField(default='fas fa-object-group', max_length=64),
        ),
        migrations.AddField(
            model_name='module',
            name='icone',
            field=models.CharField(default='fas fa-puzzle-piece', max_length=64),
        ),
        migrations.AddField(
            model_name='profession',
            name='icone',
            field=models.CharField(default='fas fa-briefcase', max_length=64),
        ),
    ]
