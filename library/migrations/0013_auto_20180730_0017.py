# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-30 00:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_auto_20180729_2301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='externalmodule',
            name='command',
        ),
        migrations.AddField(
            model_name='command',
            name='external_module',
            field=models.ManyToManyField(blank=True, null=True, to='library.ExternalModule'),
        ),
    ]
