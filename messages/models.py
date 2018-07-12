from django.db import models
from django.contrib.auth.models import User, Group
from bots.models import Bot

class Message(models.Model):
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
    group = models.ForeignKey(Group, null=True, on_delete=models.DO_NOTHING)
    bot = models.ForeignKey(Bot, null=True, on_delete=models.DO_NOTHING)
    code = models.CharField(max_length = 16, default='')
    title = models.CharField(max_length = 256)
    text = models.CharField(max_length = 4096)
    creation_time = models.DateTimeField()
    read_date = models.DateTimeField()
    def clean(self):
        input_count = 0
        if self.user:
            input_count+=1
        if self.group:
            input_count+=1
        if self.bot:
            input_count+=1
        if input_count>1:
            raise ValidationError('Original receiver can either be a bot, a user, or a group.')
        elif input_count==0:
            raise ValidationError('Original receiver is not specified.')

class CarbonCopy(models.Model):
    message = models.ForeignKey(message, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
    group = models.ForeignKey(Group, null=True, on_delete=models.DO_NOTHING)
    bot = models.ForeignKey(Bot, null=True, on_delete=models.DO_NOTHING)
    read_date = models.DateTimeField()
