from django.core import serializers
from django.http import JsonResponse
from django.utils import timezone
from django.shortcuts import render
from bots.models import Bot
from .models import Profession, Module, Category, ExternalModule, Command, Call, Word, Combo

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


#__________________________________________________________________________________________________________________________
#--------------------------------------------------------------------------------------------------------------------------
#__________________________________________________________________________________________________________________________
def update_profession(request, **kwargs):
    try:
        result = {}
        bot = Bot.objects.get(name=request.POST.get('bot_name'), code=request.POST.get('bot_code'), connection_code=request.POST.get('conn_code'))
        if bot is not None:
            kwargs['profession']=Profession.objects.get(code = kwargs['profession_code'])
            kwargs['modules']=Module.objects.filter(profession = kwargs['profession'])
            result['commands_codes']=list(Command.objects.filter(module__in = kwargs['modules']).values('code'))
    except Module.DoesNotExist:
        kwargs['error'] = 'There are no categories with code: {0}'.format(kwargs['bot_name'],)
    return JsonResponse(result)

def download_command(request, **kwargs):
    try:
        result = {}
        bot = Bot.objects.get(name=request.POST.get('bot_name'), code=request.POST.get('bot_code'), connection_code=request.POST.get('conn_code'))
        if bot is not None:
            command_object=Command.objects.get(code = kwargs['command_code'])
            command_data_object=Command.objects.filter(code = kwargs['command_code']).values()[0]
            try:
                categories_list = list(Category.objects.filter(command=command_object).values('name', 'code', 'picture', 'description'))
            except Category.DoesNotExist:
                kwargs['error'] =  'Category {0} does not have any commands.'.format(kwargs['Category_code'],)
            try:
                calls_list = list(Call.objects.filter(command=command_object).values())
            except Call.DoesNotExist:
                pass


            result['command']=command_data_object
            result['command']['module_name']=command_object.module.name

            result['command']['categories']=categories_list

            
            result['command']['note']='Imported from peak_30 {0}.'.format(timezone.now(),)

            result['command'].pop('id', None)
            result['command'].pop('module_id', None)
            result['command'].pop('creator_id', None)

            result['command']['external_modules'] = list()
            
            for external_module in command_object.external_modules.all():
                result['command']['external_modules'].append(external_module.name)


            result['command']['calls']=list()


            for call_object in calls_list:
                combos = Combo.objects.filter(call_id=call_object['id'])
                call_object['words']=list()
                for combo in combos:
                    word = (Word.objects.filter(id=combo.word_id).values('text'))[0]
                    word['position']=combo.position
                    word['optional']=combo.optional
                    word['varible_length']=combo.variable_length

                    call_object['words'].append(word)

                result['command']['calls'].append(call_object)

    except Module.DoesNotExist:
        kwargs['error'] = 'There are no categories with code: {0}'.format(kwargs['category_code'],)
    return JsonResponse(result)
