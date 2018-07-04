from django.contrib import admin
from .models import UserProfile, GroupProfile, BotProfile

admin.site.register((UserProfile, GroupProfile, BotProfile))
