from django.shortcuts import render
#from django.contrib.auth.models import User, Group
from profiles.models import UserProfile, GroupProfile
from bots.models import Bot
from library.models import Profession, Module, Command
from schedule.models import TimeSpan

def get_dashboard(request, **kwargs):
    kwargs['group_profiles'] = GroupProfile.objects.all()
    kwargs['user_profiles'] = UserProfile.objects.all()
    kwargs['bots'] = Bot.objects.all()
    kwargs['professions'] = Profession.objects.all()
    kwargs['modules'] = Module.objects.all()
    kwargs['timespans'] = TimeSpan.objects.all()
    return render(request, 'dashboard.html', kwargs)
