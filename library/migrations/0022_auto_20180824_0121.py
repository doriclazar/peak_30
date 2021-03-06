# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-08-24 01:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0021_auto_20180821_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('code', models.CharField(default='', max_length=16)),
                ('active', models.BooleanField(default=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='library.Module')),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='code',
            field=models.CharField(default='CA-1652', max_length=16, unique=True),
        ),
    ]
