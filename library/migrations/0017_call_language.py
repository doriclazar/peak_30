# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-31 06:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0016_auto_20180731_0611'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='language',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='library.Language'),
            preserve_default=False,
        ),
    ]
