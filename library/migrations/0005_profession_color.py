# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-16 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20180704_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='profession',
            name='color',
            field=models.CharField(default='ffcf9e', max_length=8),
        ),
    ]
