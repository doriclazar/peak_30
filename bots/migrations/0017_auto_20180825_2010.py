# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-08-25 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0016_auto_20180825_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot',
            name='code',
            field=models.CharField(default='BOT-2840', max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='rule',
            name='code',
            field=models.CharField(default='RUL-1536', max_length=8, unique=True),
        ),
    ]
