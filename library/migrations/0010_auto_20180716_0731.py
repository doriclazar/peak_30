# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-16 07:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_auto_20180716_0730'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='icone',
            new_name='icon',
        ),
        migrations.RenameField(
            model_name='module',
            old_name='icone',
            new_name='icon',
        ),
        migrations.RenameField(
            model_name='profession',
            old_name='icone',
            new_name='icon',
        ),
    ]
