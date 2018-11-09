from django.contrib import admin
from .models import Event, Action, ActionType
admin.site.register((Event, Action, ActionType))

