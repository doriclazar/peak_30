# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-30 20:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('bots', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bot_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.URLField(default='http://i0.wp.com/cdn.techgyd.com/save-whatsapp-profile-picture-image3.jpg')),
                ('about', models.CharField(default=None, max_length=4096)),
                ('rating', models.FloatField(default=0)),
                ('creation_date', models.DateField()),
                ('bot', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='bots.Bot')),
            ],
        ),
        migrations.CreateModel(
            name='Group_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.URLField(default='http://i0.wp.com/cdn.techgyd.com/save-whatsapp-profile-picture-image3.jpg')),
                ('about', models.CharField(default=None, max_length=4096)),
                ('rating', models.FloatField(default=0)),
                ('peak_points', models.FloatField(default=0)),
                ('creation_date', models.DateField()),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.URLField(default='http://i0.wp.com/cdn.techgyd.com/save-whatsapp-profile-picture-image3.jpg')),
                ('about', models.CharField(default=None, max_length=4096)),
                ('rating', models.FloatField(default=0)),
                ('birth_date', models.DateField(default=None)),
                ('address_line_1', models.CharField(max_length=128)),
                ('address_line_2', models.CharField(max_length=128)),
                ('phone_number', models.CharField(max_length=16)),
                ('peak_points', models.FloatField(default=0)),
                ('creation_date', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='personal_info',
            name='user_account',
        ),
        migrations.RemoveField(
            model_name='public_info',
            name='user_account',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='user_account',
        ),
        migrations.DeleteModel(
            name='Personal_Info',
        ),
        migrations.DeleteModel(
            name='Public_Info',
        ),
        migrations.DeleteModel(
            name='Settings',
        ),
    ]
