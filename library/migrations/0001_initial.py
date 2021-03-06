# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-03 02:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.URLField(default='')),
                ('name', models.CharField(max_length=32)),
                ('code', models.CharField(default='', max_length=16)),
                ('description', models.CharField(max_length=1024)),
                ('creation_date', models.DateField()),
                ('active', models.BooleanField(default=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('code', models.CharField(default='', max_length=16)),
                ('programming_language', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=1024)),
                ('definition', models.CharField(max_length=8192)),
                ('script_url', models.CharField(max_length=128)),
                ('creation_date', models.DateField()),
                ('active', models.BooleanField(default=True)),
                ('categories', models.ManyToManyField(to='library.Category')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.URLField(default='')),
                ('name', models.CharField(max_length=32)),
                ('code', models.CharField(default='', max_length=16)),
                ('description', models.CharField(max_length=1024)),
                ('active', models.BooleanField(default=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.URLField(default='')),
                ('name', models.CharField(max_length=32)),
                ('code', models.CharField(default='', max_length=16)),
                ('description', models.CharField(max_length=1024)),
                ('creation_date', models.DateField()),
                ('active', models.BooleanField(default=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='module',
            name='professions',
            field=models.ManyToManyField(to='library.Profession'),
        ),
        migrations.AddField(
            model_name='command',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='library.Module'),
        ),
    ]
