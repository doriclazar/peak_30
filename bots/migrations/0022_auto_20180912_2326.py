# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-09-12 23:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0021_auto_20180825_2049'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bot',
            options={'verbose_name': 'Bot', 'verbose_name_plural': 'Bots'},
        ),
        migrations.AlterModelOptions(
            name='permit',
            options={'verbose_name': 'Permit', 'verbose_name_plural': 'Permits'},
        ),
        migrations.AlterModelOptions(
            name='rule',
            options={'verbose_name': 'Rule', 'verbose_name_plural': 'Rules'},
        ),
    ]
