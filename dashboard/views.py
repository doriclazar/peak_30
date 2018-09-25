from django.shortcuts import render
#from django.contrib.auth.models import User, Group
from profiles.models import UserProfile, GroupProfile
from bots.models import Bot
from library.models import Profession, Module, Category, Command
from schedule.models import TimeSpan
from .models import UserSettings

def get_dashboard(request, **kwargs):

    users_settigs = UserSettings.objects.filter(user = auth.user)

    kwargs['group_profiles'] = GroupProfile.objects.all()
    kwargs['user_profiles'] = UserProfile.objects.all()
    kwargs['professions'] = Profession.objects.all()
    kwargs['modules'] = Module.objects.all()
    kwargs['categories'] = Category.objects.all()
    kwargs['commands'] = Command.objects.all()
    kwargs['timespans'] = TimeSpan.objects.all()
    kwargs['bots'] = Bot.objects.all()

    worked_timespans = []
    for bot in kwargs['bots']:
        for index in range(int(user_settigs[0]['chart_period'])):
            pass
        #worked_timespans.append(TimeSpan.objects.filter(bot = bot, end_date before 2m ago & after 3m ago, is_skip=False).values('id'))
        #worked_timespans.append(TimeSpan.objects.filter(bot = bot, end_date before 2m ago & after 3m ago, is_skip=False).values('id'))
        #worked_timespans.append(TimeSpan.objects.filter(bot = bot, end_date before 1m ago & after 2m ago, is_skip=False).values('id'))
        #worked_timespans.append(TimeSpan.objects.filter(bot = bot, end_date before today & after 1m ago, is_skip=False).values('id'))
        #for timespan in worked_timespans:
        #    bot.numdata.append(len(timespan))
        
        #time_worked = timesince(worked_timespans.date_start) - timesince(worked_timespans.date_end) - 24*(7 - (worked_timespans.end_day - worked_timespans.start_day)) - (timesince(worked_timespans.start_time) - timesince(worked_timespans.end_time))

    #for bot_index in range(len(kwargs['bots'])):
        #worked_timespans =  TimeSpan.objects.filter(bot = kwargs['bots'][bot_index], is_skip=False).values('start_day', 'end_day', 'start_date', 'end_date', 'start_time', 'end_time')
        #kwargs['bots'][bot_index]
    
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
