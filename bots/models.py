import re
from django.db import models
from django.contrib.auth.models import User, Group

class Profession(models.Model):
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length = 128)
    code = models.CharField(max_length = 128, default='')
    active = models.BooleanField(default = True)
    def __str__(self):
        return 'Profession: {0}.  Creator: {1}.'.format(self.name, self.creator.get_full_name())

    def clean(self):
        forbiden_chars = (' ', '!', '$', '^', '*')
        for forbiden_char in forbiden_chars:
            if forbiden_char in self.code:
                raise ValidationError('Profession code must not contain {0} character.'.format(forbiden_char,))

class Bot(models.Model):
    creator = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    profession = models.ManyToManyField(Profession)
    name = models.CharField(max_length = 128)
    code = models.CharField(max_length = 128, default='')
    public_key = models.CharField(max_length = 4096)
    public_key_expiry = models.DateField()
    active = models.BooleanField(default = True)
    def __str__(self):
        return 'Bot: {0}.  Creator: {1}.'.format(self.name, self.creator.get_full_name())

class Rule(models.Model):
    name = models.CharField(max_length = 64)
    code = models.CharField(max_length = 8)
    active = models.BooleanField(default = True)
    def __str__(self):
        return 'Rule: {0}.  Code: {1}.'.format(self.name, self.code)


class Permit(models.Model):
    user = models.ForeignKey(User, blank=True, on_delete = models.DO_NOTHING) 
    group = models.ForeignKey(Group, blank=True, on_delete = models.DO_NOTHING) 
    bot = models.ForeignKey(Bot, blank=True, null=True, on_delete = models.DO_NOTHING) 
    profession = models.ForeignKey(Profession, blank=True, null=True, on_delete = models.DO_NOTHING) 
    rule = models.ForeignKey(Rule, on_delete = models.DO_NOTHING) 
    issued_datetime = models.DateTimeField()
    expiry_datetime = models.DateTimeField(null=True)
    active = models.BooleanField(default = True)
    def clean(self):
        if not self.user and not self.group:
            raise ValidationError('Either "user" or "group" is required.')
        elif not self.user and not self.group:
            raise ValidationError('Can issue permit only to "user" OR "group". Not both.')

        if not self.bot and not self.profession:
            raise ValidationError('Either "bot" or "profession" is required.')
        elif self.bot and self.profession:
            raise ValidationError('A single permit can be issued only for "bot" OR "profession". Not both.')

    def __str__(self):
        return 'user {0} or group {1} {2} {3}'.format(self.user.get_full_name(), self.group.name, self.rule.name, self.bot.name)
