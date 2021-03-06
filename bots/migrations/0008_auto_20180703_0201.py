# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-03 02:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20180703_0201'),
        ('bots', '0007_auto_20180701_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profession',
            name='creator',
        ),
        migrations.AlterField(
            model_name='bot',
            name='code',
            field=models.CharField(default='', max_length=16),
        ),
        migrations.AlterField(
            model_name='bot',
            name='name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='bot',
            name='profession',
            field=models.ManyToManyField(to='library.Profession'),
        ),
        migrations.AlterField(
            model_name='bot',
            name='public_key',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='permit',
            name='profession',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='library.Profession'),
        ),
        migrations.AlterField(
            model_name='rule',
            name='code',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='rule',
            name='name',
            field=models.CharField(max_length=32),
        ),
        migrations.DeleteModel(
            name='Profession',
        ),
    ]
