from django.contrib import admin
from .models import Bot, Rule, Permit

admin.site.register((Bot, Rule, Permit))
