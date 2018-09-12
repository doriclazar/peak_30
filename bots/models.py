import uuid
from django.db import models
from django.contrib.auth.models import User, Group
from library.models import Profession

class Bot(models.Model):
    creator = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    profession = models.ManyToManyField(Profession)
    name = models.CharField(max_length = 32)
    code = models.UUIDField(default=uuid.uuid4, editable=False)
    connection_code = models.CharField(max_length = 8, default='00000000')
    rating = models.FloatField(default = 0)
    public_key = models.CharField(max_length = 1024)
    public_key_expiry = models.DateField()
    creation_date = models.DateField()
    accept_appointment = models.BooleanField(default = True)
    active = models.BooleanField(default = True)
    def __str__(self):
        return 'Bot: {0}.  Creator: {1}.'.format(self.name, self.creator.get_full_name())
    class Meta:
        verbose_name = "Bot"
        verbose_name_plural = "Bots"

class Rule(models.Model):
    name = models.CharField(max_length = 32)
    code = models.UUIDField(default=uuid.uuid4, editable=False)
    active = models.BooleanField(default = True)

    def __str__(self):
        return 'Rule: {0}.  Code: {1}.'.format(self.name, self.code)

    class Meta:
        verbose_name = "Rule"
        verbose_name_plural = "Rules"


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

    class Meta:
        verbose_name = "Permit"
        verbose_name_plural = "Permits"
