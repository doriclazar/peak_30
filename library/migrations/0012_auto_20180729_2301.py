# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-29 23:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0011_auto_20180723_2332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ignoreresponse',
            name='initial_call',
        ),
        migrations.RemoveField(
            model_name='ignoreresponse',
            name='response',
        ),
        migrations.DeleteModel(
            name='IgnoreResponse',
        ),
    ]
