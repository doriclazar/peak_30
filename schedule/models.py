from django.db import models
from django.contrib.auth.models import User, Group
from bots.models import Bot
from library.models import Command

class Appointment(models.Model):
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='appointment_creator')
    user = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING, related_name='appointment_user')
    group = models.ForeignKey(Group, null=True, on_delete=models.DO_NOTHING)
    bot = models.ForeignKey(Bot, null=True, on_delete=models.DO_NOTHING)
    code = models.CharField(max_length = 16, default='')
    description = models.CharField(max_length = 1024)
    creation_time = models.DateTimeField()
    read_time = models.DateTimeField(null=True)
    active = models.BooleanField(default=True)
    def clean(self):
        input_count = 0
        if self.user:
            input_count+=1
        if self.group:
            input_count+=1
        if self.bot:
            input_count+=1
        if input_count>1:
            raise ValidationError('Original receiver can either be a bot, a user, or a group.')
        elif input_count==0:
            raise ValidationError('Original receiver is not specified.')

class TimeLine(models.Model):
    '''
    Represents the date and time at which the appointment is active.
    "is_skip" variable overlays active time from other record as a pause in activity.
    '''
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    DAYS_OF_WEEK = (
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
        )
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    start_day = models.IntegerField(choices = DAYS_OF_WEEK, null=True)
    end_day = models.IntegerField(choices = DAYS_OF_WEEK, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    is_skip = models.BooleanField(default=False)
    def clean(self):
        if not self.start_day and self.end_day:
            raise ValidationError('Need a start day.')
        if not self.start_date and self.end_date:
            raise ValidationError('Need a start date.')
        if (not self.start_time and self.end_time) or (self.start_time and not self.end_time):
            raise ValidationError('Time must be defined with "from" - "until" varibales.')
        if self.start_day and self.start_date:
            raise ValidationError('"Date" and "Day" varibles are mutualy exclusive for timeline.')
        if not self.start_day and not self.start_date and not self.start_time:
            raise ValidationError('Timeline input does not contain any time values.')

class AppointmentCommand(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete = models.CASCADE)
    command = models.ForeignKey(Command, on_delete = models.DO_NOTHING)
    description = models.CharField(max_length = 1024)

