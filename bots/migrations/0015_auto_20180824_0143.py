# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-08-24 01:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0014_bot_connection_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot',
            name='code',
            field=models.CharField(default='BOT-6882', max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='bot',
            name='connection_code',
            field=models.CharField(default='00000000', max_length=8),
        ),
        migrations.AlterField(
            model_name='rule',
            name='code',
            field=models.CharField(default='RUL-5470', max_length=8, unique=True),
        ),
    ]
