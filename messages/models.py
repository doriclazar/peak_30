import uuid
from django.db import models
from django.contrib.auth.models import User, Group
from bots.models import Bot

class Message(models.Model):
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='message_creator')
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING, related_name='message_user')
    group = models.ForeignKey(Group, null=True, blank=True, on_delete=models.DO_NOTHING)
    bot = models.ForeignKey(Bot, null=True, blank=True, on_delete=models.DO_NOTHING)
    code = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length = 256)
    text = models.CharField(max_length = 4096)
    creation_time = models.DateTimeField()
    read_date = models.DateTimeField(null=True, blank=True)
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
    message = models.ForeignKey(Message, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    group = models.ForeignKey(Group, null=True, blank=True, on_delete=models.DO_NOTHING)
    bot = models.ForeignKey(Bot, null=True, blank=True, on_delete=models.DO_NOTHING)
    read_date = models.DateTimeField()
