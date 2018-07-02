from django.contrib import admin
from .models import Profession, Bot, Rule, Permit

admin.site.register((Profession, Bot, Rule, Permit))
