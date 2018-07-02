from django.contrib import admin
from .models import UserProfile, GroupProfile, ProfessionProfile, BotProfile

admin.site.register((UserProfile, GroupProfile, ProfessionProfile, BotProfile))
