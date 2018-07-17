from django.contrib import admin
from .models import Event, TimeSpan, EventCommand

admin.site.register((Event, TimeSpan, EventCommand))

