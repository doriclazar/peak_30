import uuid
from django.db import models
from django.contrib.auth.models import User, Group
from bots.models import Bot
from library.models import Profession, Command

class ActionType(models.Model):
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length = 32)
    description = models.CharField(max_length = 1024)
    active = models.BooleanField(default=True)

    def __str__(self):
       return '{0}'.format(self.name)

    class Meta:
        verbose_name = "Action Type"
        verbose_name_plural = "Action Types"

class Event(models.Model):
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length = 32)
    code = models.UUIDField(default=uuid.uuid4, editable=False)
    description = models.CharField(max_length = 1024)
    creation_time = models.DateTimeField()
    read_time = models.DateTimeField(null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
       return '{0} {1} {2}'.format(self.creator, self.name, self.creation_time)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

class Action(models.Model):
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='timespan_creator')
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    action_type = models.ForeignKey(ActionType, on_delete=models.CASCADE)
    name = models.CharField(max_length = 32)
    command = models.ForeignKey(Command, on_delete = models.DO_NOTHING)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    group = models.ForeignKey(Group, null=True, blank=True, on_delete=models.DO_NOTHING)
    bot = models.ForeignKey(Bot, null=True, blank=True, on_delete=models.DO_NOTHING)
    profession = models.ForeignKey(Profession, null=True, blank=True, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length = 1024, null=True, blank=True)

    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)

    def clean(self):
        input_count = 0
        if self.user:
            input_count+=1
        if self.group:
            input_count+=1
        if self.bot:
            input_count+=1
        if self.profession:
            input_count+=1
        if input_count>1:
            raise ValidationError('Original receiver can either be a bot, a user, or a group.')
        elif input_count==0:
            raise ValidationError('Original receiver is not specified.')

    def get_actor_name(self):
        if self.user:
            actor_name=self.user.get_full_name()
        elif self.group:
            actor_name=self.group.name
        elif self.bot:
            actor_name=self.bot.name
        elif self.profession:
            actor_name=self.profession.name
        return actor_name

    def get_actor_icon(self):
        if self.user:
            actor_icon='fas fa-user'
        elif self.group:
            actor_icon='fas fa-users'
        elif self.bot:
            actor_icon='fas fa-robot'
        elif self.profession:
            actor_icon='fas fa-briefcase'
        return actor_icon

    def get_actor_color(self):
        if self.user:
            actor_color=self.user.user_profile.color
        elif self.group:
            actor_color=self.group.group_profile.color
        elif self.bot:
            actor_color=self.bot.bot_profile.color
        elif self.profession:
            actor_color=self.profession.color
        return actor_color

    def __str__(self):
        return '{0} {1} {2}'.format(self.name, self.command.name, self.get_actor_name())

    class Meta:
        verbose_name = "Action"
        verbose_name_plural = "Actions"
