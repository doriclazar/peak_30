from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from bots.models import Bot
from .models import Profession, Module, Category, Command

def index(request, **kwargs):
    return render(request, 'library/index.html', kwargs)

def get_professions(request, **kwargs):
    kwargs['professions'] = Profession.objects.all()
    return render(request, 'library/professions.html', kwargs)

def get_modules(request, **kwargs):
    kwargs['modules'] = Module.objects.all()
    return render(request, 'library/modules.html', kwargs)

def get_categories(request, **kwargs):
    kwargs['categories'] = Category.objects.all()
    return render(request, 'library/categories.html', kwargs)

def get_commands(request, **kwargs):
    kwargs['commands'] = Command.objects.all()
    return render(request, 'library/commands.html', kwargs)


def get_profession(request, **kwargs):
    try:
        kwargs['profession'] = Profession.objects.get(code = kwargs['profession_code'])
        try:
            kwargs['bots'] = Bot.objects.filter(profession = kwargs['profession'])
        except Bot.DoesNotExist:
            kwargs['error'] = 'There are bots no with profession code: {0}'.format(kwargs['profession_code'],)

        try:
            kwargs['modules'] = Module.objects.filter(profession = kwargs['profession'])
        except Module.DoesNotExist:
            kwargs['error'] = 'There are modules no with profession code: {0}'.format(kwargs['profession_code'],)

    except Profession.DoesNotExist:
        kwargs['error'] = 'There are no professions with code: {0}'.format(kwargs['profession_code'],)
    return render(request, 'library/profession.html', kwargs)

def get_module(request, **kwargs):
    try:
        kwargs['module'] = Module.objects.get(code = kwargs['module_code'])
        try:
            kwargs['commands'] = Command.objects.filter(module = kwargs['module'])
        except Command.DoesNotExist:
            kwargs['error'] =  'Module {0} does not have any commands.'.format(kwargs['profession_code'],)

    except Module.DoesNotExist:
        kwargs['error'] = 'There are no modules with code: {0}'.format(kwargs['module_code'],)
    return render(request, 'library/module.html', kwargs)

def get_category(request, **kwargs):
    try:
        kwargs['category'] = Category.objects.get(code = kwargs['module_code'])
        try:
            kwargs['commands'] = Command.objects.filter(category = kwargs['Category'])
        except Command.DoesNotExist:
            kwargs['error'] =  'Category {0} does not have any commands.'.format(kwargs['Category_code'],)

    except Category.DoesNotExist:
        kwargs['error'] = 'There are no categories with code: {0}'.format(kwargs['category_code'],)
    return render(request, 'library/category.html', kwargs)

def get_command(request, **kwargs):
    try:
        kwargs['command'] = Command.objects.get(code = kwargs['command_code'])
        try:
            kwargs['categories'] = Category.objects.filter(command = kwargs['command'])
        except Category.DoesNotExist:
            kwargs['error'] =  'Category {0} does not have any commands.'.format(kwargs['Category_code'],)

    except Module.DoesNotExist:
        kwargs['error'] = 'There are no categories with code: {0}'.format(kwargs['category_code'],)
    return render(request, 'library/command.html', kwargs)

def download_command(request, **kwargs):
    try:
        result = {}
        bot = Bot.objects.get(name = request.POST.get('bot_name'), connection_code = request.POST.get('connection_code'))
        if bot is not None:
            kwargs['command']=Command.objects.get(code = kwargs['command_code'])
            kwargs['command_data']=Command.objects.filter(code = kwargs['command_code']).values()[0]
            try:
                kwargs['categories'] = list(Category.objects.filter(command = kwargs['command']).values())
            except Category.DoesNotExist:
                kwargs['error'] =  'Category {0} does not have any commands.'.format(kwargs['Category_code'],)


            result['command']=kwargs['command_data']
            result['command']['categories']=kwargs['categories']



    except Module.DoesNotExist:
        kwargs['error'] = 'There are no categories with code: {0}'.format(kwargs['category_code'],)
    return JsonResponse(result)
