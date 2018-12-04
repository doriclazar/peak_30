from datetime import datetime, timedelta
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from profiles.models import UserProfile, GroupProfile
from bots.models import Bot
from library.models import Profession, Module, Category, Command
from schedule.models import Event, Action
from .models import UserSettings

def get_dashboard(request, **kwargs):
    user_settings=(None,)
    '''
    if request.user.is_authenticated:
        user_settings = UserSettings.objects.filter(user = request.user)
    else: 
        user_settings = UserSettings.objects.filter(user = 'default')
    '''

    # Modify to return the values by auth.user, not .all():
    kwargs['group_profiles'] = GroupProfile.objects.all()
    kwargs['user_profiles'] = UserProfile.objects.all()
    kwargs['professions'] = Profession.objects.all()
    kwargs['modules'] = Module.objects.all()
    kwargs['categories'] = Category.objects.all()
    kwargs['commands'] = Command.objects.all()
    kwargs['actions'] = Action.objects.all()
    kwargs['bots'] = Bot.objects.all()

    done_actions = []
    for bot in kwargs['bots']:
        pass
        # Modify to extract by key name, not index:


        '''
        for index in range(int(user_settings[0]['chart_period'])):
            pass
        '''
    kwargs['events'] = Event.objects.filter(active=True)
    kwargs['actions'] = {'done':[], 'in_progress':[], 'archived':[]}
    for kw_event in kwargs['events']:
        kwargs['actions']['done'].append(Action.objects.filter(event=kw_event, completion=100))
        kwargs['actions']['in_progress'].append(Action.objects.filter(event=kw_event, completion__lt=100))
        kwargs['actions']['archived'].append(Action.objects.filter(event=kw_event, end_time__lt=datetime.now() - timedelta(days=7)))
        #.append(Action.objects.filter(event=kw_event))

        #done_actions.append(Action.objects.filter(bot = bot, end_date before 2m ago & after 3m ago, is_skip=False).values('id'))
        #done_actions.append(Action.objects.filter(bot = bot, end_date before 2m ago & after 3m ago, is_skip=False).values('id'))
        #finished_events.append(TimeSpan.objects.filter(bot = bot, end_date before 2m ago & after 3m ago, is_skip=False).values('id'))
        #finished_events.append(TimeSpan.objects.filter(bot = bot, end_date before 1m ago & after 2m ago, is_skip=False).values('id'))
        #finished_events.append(TimeSpan.objects.filter(bot = bot, end_date before today & after 1m ago, is_skip=False).values('id'))
        for done_action in done_actions:
            bot.numdata.append(len(done_action))
        
    '''
    finished_events =  Schedule.objects.filter(is_skip=False).values('start_day, end_day, start_date, end_date')
    time_worked = timesince(finished_events.date_start) - timesince(finished_events.date_end) + 

    idled_timespans =  Schedule.objects.filter(is_skip=True).values('start_day, end_day, start_date, end_date')
    time_idled = timesince(idled_timespans.date_start) - timesince(idled_timespans.date_end) +

    total_time = '3m'
    time_free = total_time - time_worked - time_idled    

    kwargs['time_consumption_numdata'] = [time_worked, time_idled, time_free]  
    '''
    #    time_worked = timesince(done_actions.date_start) - timesince(done_actions.date_end) - 24*(7 - (done_actions.end_day - done_actions.start_day)) - (timesince(done_actions.start_time) - timesince(done_actions.end_time))

    #for bot_index in range(len(kwargs['bots'])):
        #done_events =  Event.objects.filter(bot = kwargs['bots'][bot_index], is_skip=False).values('start_day', 'end_day', 'start_date', 'end_date', 'start_time', 'end_time')
        #kwargs['bots'][bot_index]
    
    # Rebuild the view to project Event/Action models (timespans are no longer active).
    '''

    '''
    return render(request, 'dashboard.html', kwargs)
