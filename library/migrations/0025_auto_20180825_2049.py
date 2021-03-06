# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-08-25 20:49
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0024_auto_20180825_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='code',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='category',
            name='code',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='class',
            name='code',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='command',
            name='code',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='module',
            name='code',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='profession',
            name='code',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
