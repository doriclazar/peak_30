from django.db import models
from django.contrib.auth.models import User, Group
from bots.models import Bot
from library.models import Profession
import datetime

class GroupProfile(models.Model):
    group = models.OneToOneField(Group, on_delete = models.DO_NOTHING, related_name='group_profile')
    picture = models.URLField(default = '')
    color = models.CharField(max_length=8, default='fafad2')
    about = models.CharField(max_length = 1024, default = None)
    rating = models.FloatField(default = 0)
    #Keep private
    peak_points = models.FloatField(default = 0)
    #
    creation_date = models.DateField()
    def __str__(self):
       return '{0}'.format(self.group.name)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.DO_NOTHING, related_name='user_profile')
    picture = models.URLField(default = '')
    color = models.CharField(max_length=8, default='00bfff')
    about = models.CharField(max_length = 1024, default = None)
    rating = models.FloatField(default = 0)
    birth_date = models.DateField(default = None)
    #Keep private
    address_line_1 = models.CharField(max_length = 128)
    address_line_2 = models.CharField(max_length = 128)
    phone_number = models.CharField(max_length = 16)
    peak_points = models.FloatField(default = 0)
    #
    creation_date = models.DateField()
    def __str__(self):
       return '{0} {1} {2}'.format(self.user.email, self.user.first_name, self.user.last_name)

class BotProfile(models.Model):
    bot = models.OneToOneField(Bot, on_delete = models.DO_NOTHING, related_name='bot_profile')
    picture = models.URLField(default = '')
    color = models.CharField(max_length=8, default='90EE90')
    about = models.CharField(max_length = 1024, default = None)
    rating = models.FloatField(default = 0)
    creation_date = models.DateField()
    def __str__(self):
       return '{0}'.format(self.bot.name)
