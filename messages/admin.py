from django.contrib import admin
from .models import Message, CarbonCopy

admin.site.register((Message, CarbonCopy))
