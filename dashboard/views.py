from django.shortcuts import render
#from django.contrib.auth.models import User, Group
from profiles.models import UserProfile, GroupProfile
from bots.models import Bot
from library.models import Profession, Module, Category, Command
from schedule.models import TimeSpan

def get_dashboard(request, **kwargs):
    kwargs['group_profiles'] = GroupProfile.objects.all()
    kwargs['user_profiles'] = UserProfile.objects.all()
    kwargs['professions'] = Profession.objects.all()
    kwargs['modules'] = Module.objects.all()
    kwargs['categories'] = Category.objects.all()
    kwargs['commands'] = Command.objects.all()
    kwargs['timespans'] = TimeSpan.objects.all()
    kwargs['bots'] = Bot.objects.all()
    kwargs['bots_numdata'] = []
    for bot_data in kwargs['bots']:
        worked_timespans =  TimeSpan.objects.filter(bot = bot_data, is_skip=False).values('start_day', 'end_day', 'start_date', 'end_date', 'start_time', 'end_time')
        #bot_time_worked = timesince(bot_worked_timespans.date_start) - timesince(bot_worked_timespans.date_end) - 24*(7 - (end_day - start_day)) - (timesince(start_time) - timesince(end_time))
        #bot_time_idled = 
        #bot_time_free =
        bot_numdata = [1, 1, 1]
        kwargs['bots_numdata'].append(bot_numdata)
    
    '''
    worked_timespans =  Schedule.objects.filter(is_skip=False).values('start_day, end_day, start_date, end_date')
    time_worked = timesince(worked_timespans.date_start) - timesince(worked_timespans.date_end) + 

    idled_timespans =  Schedule.objects.filter(is_skip=True).values('start_day, end_day, start_date, end_date')
    time_idled = timesince(idled_timespans.date_start) - timesince(idled_timespans.date_end) +

    total_time = '3m'
    time_free = total_time - time_worked - time_idled    

    kwargs['time_consumption_numdata'] = [time_worked, time_idled, time_free]  

    '''
    return render(request, 'dashboard.html', kwargs)
