from django.db import models
from django.contrib.auth.models import User

class Profession(models.Model):
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    picture = models.URLField(default = '')
    name = models.CharField(max_length = 32)
    code = models.CharField(max_length = 16, default='')
    description = models.CharField(max_length = 1024)
    creation_date = models.DateField()
    active = models.BooleanField(default = True)
    def __str__(self):
        return 'Profession: {0}.  Creator: {1}.'.format(self.name, self.creator.get_full_name())

    def clean(self):
        forbiden_chars = (' ', '!', '$', '^', '*')
        for forbiden_char in forbiden_chars:
            if forbiden_char in self.code:
                raise ValidationError('Profession code must not contain {0} character.'.format(forbiden_char,))

class Module(models.Model):
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    profession = models.ForeignKey(Profession, on_delete=models.DO_NOTHING)
    picture = models.URLField(default = '')
    name = models.CharField(max_length = 32)
    code = models.CharField(max_length = 16, default='')
    description = models.CharField(max_length = 1024)
    active = models.BooleanField(default = True)
    def __str__(self):
        return 'Module: {0}.  Creator: {1}.'.format(self.name, self.creator.get_full_name())

class Category(models.Model):
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    picture = models.URLField(default = '')
    name = models.CharField(max_length = 32)
    code = models.CharField(max_length = 16, default='')
    description = models.CharField(max_length = 1024)
    creation_date = models.DateField()
    active = models.BooleanField(default = True)
    def __str__(self):
        return 'Category: {0}.  Creator: {1}.'.format(self.name, self.creator.get_full_name())

class Command(models.Model):
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    module = models.ForeignKey(Module, on_delete=models.DO_NOTHING)
    categories = models.ManyToManyField(Category)
    name = models.CharField(max_length = 32)
    code = models.CharField(max_length = 16, default='')
    programming_language = models.CharField(max_length=32)
    description = models.CharField(max_length = 1024)
    definition = models.CharField(max_length=8192)
    script_url = models.CharField(max_length=128)
    creation_date = models.DateField()
    active = models.BooleanField(default = True)
    def __str__(self):
        return 'Category: {0}.  Creator: {1}.'.format(self.name, self.creator.get_full_name())

