from django.shortcuts import render
from django.contrib.auth.models import User, Group
from datetime import date
from bots.models import Profession, Bot
from .models import UserProfile, GroupProfile, BotProfile

def index(request, **kwargs):
    return render(request, 'profiles/index.html', kwargs)

def get_users(request, **kwargs):
    kwargs['users'] = User.objects.all()
    return render(request, 'profiles/users.html', kwargs)


def get_groups(request, **kwargs):
    kwargs['groups'] = Group.objects.all()
    return render(request, 'profiles/groups.html', kwargs)


def get_bots(request, **kwargs):
    kwargs['bots'] = Bot.objects.all()
    return render(request, 'profiles/bots.html', kwargs)

def get_group_profile(request, **kwargs):
    try:
        kwargs['group'] = Group.objects.get(name = kwargs['group_name'])
        try:
            kwargs['profile'] = GroupProfile.objects.get(group = kwargs['group'])
            kwargs['users'] = User.objects.filter(groups = kwargs['group'])
        except GroupProfile.DoesNotExist:
            kwargs['error'] =  'Group {0} does not have a profile.'.format(kwargs['group_name'],)
    except Group.DoesNotExist:
        kwargs['error'] = 'There are no groups with name: {0}'.format(kwargs['group_name'],)
    return render(request, 'profiles/group.html', kwargs)

def get_user_profile(request, **kwargs):
    try:
        kwargs['user'] = User.objects.get(username = kwargs['username'])
        try:
            kwargs['profile'] = UserProfile.objects.get(user = kwargs['user'])
            kwargs['groups'] = Group.objects.filter(user = kwargs['user'])
            kwargs['professions'] = Profession.objects.filter(creator = kwargs['user'])
            kwargs['bots'] = Bot.objects.filter(creator = kwargs['user'])
            kwargs['age'] = date.today().year - kwargs['profile'].birth_date.year - ((date.today().month, date.today().day) \
                    < (kwargs['profile'].birth_date.month, kwargs['profile'].birth_date.day))
        except UserProfile.DoesNotExist:
            kwargs['error'] =  'User {0} does not have a profile.'.format(kwargs['username'],)
    except User.DoesNotExist:
        kwargs['error'] = 'There are no users with username: {0}'.format(kwargs['username'],)
    return render(request, 'profiles/user.html', kwargs)


def get_bot_profile(request, **kwargs):
    try:
        kwargs['bot'] = Bot.objects.get(code = kwargs['bot_code'])
        try:
            kwargs['profile'] = BotProfile.objects.get(bot = kwargs['bot'])
        except BotProfile.DoesNotExist:
            kwargs['error'] =  'Bot {0} does not have a profile.'.format(kwargs['bot_code'],)
        try:
            kwargs['professions'] = Profession.objects.filter(bot = kwargs['bot'])
        except Profession.DoesNotExist:
            kwargs['error'] = 'Bot {0} does not have any professions.'.format(kwargs['bot_code'],)

    except Bot.DoesNotExist:
        kwargs['error'] = 'There are no bots with code: {0}'.format(kwargs['bot_code'],)
    return render(request, 'profiles/bot.html', kwargs)
