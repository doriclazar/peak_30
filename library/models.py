from django.db import models
from django.contrib.auth.models import User

class Language(models.Model):
    name = models.CharField(max_length = 32)
    code = models.CharField(max_length = 8, default='')
    active = models.BooleanField(default = True)
    def __str__(self):
        return 'Language: {0}.  ISO code: {1}.'.format(self.name, self.code)

class Profession(models.Model):
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    picture = models.URLField(default = '')
    color = models.CharField(max_length=8, default='ffcf9e')
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
    creation_date = models.DateField()
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

class ExternalModule(models.Model):
    name = models.CharField(max_length = 32)
    active = models.BooleanField(default = True)
    def __str__(self):
        return 'External Module: {0}.'.format(self.name)

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
    external_modules = models.ManyToManyField(ExternalModule)
    creation_date = models.DateField()
    active = models.BooleanField(default = True)
    def __str__(self):
        return 'Command: {0}.  Creator: {1}.'.format(self.name, self.creator.get_full_name())

class Call(models.Model):
    name = models.CharField(max_length = 32)
    language = models.ForeignKey(Language, on_delete=models.DO_NOTHING)
    command = models.ForeignKey(Command)
    response = models.IntegerField()
    active = models.BooleanField(default = True)
    def __str__(self):
        return 'Command Call: {0}.'.format(self.name)

class Word(models.Model):
    text = models.CharField(max_length = 128)
    active = models.BooleanField(default = True)
    def __str__(self):
        return 'Word Text: {0}.'.format(self.text)

class Combo(models.Model):
    call = models.ForeignKey(Call, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    variable_length = models.IntegerField(default=0)
    optional = models.BooleanField(default = False)
    position = models.IntegerField()
    def __str__(self):
        return 'Call Name: {0}, Word Text: {1}.'.format(self.call.name, self.word.text)
