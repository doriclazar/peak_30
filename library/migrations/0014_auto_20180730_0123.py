# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-30 01:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0013_auto_20180730_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='command',
            name='external_module',
        ),
        migrations.AddField(
            model_name='command',
            name='external_modules',
            field=models.ManyToManyField(to='library.ExternalModule'),
        ),
    ]
