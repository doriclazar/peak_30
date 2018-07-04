from django.contrib import admin
from .models import Profession, Module, Category, Command

admin.site.register((Profession, Module, Category, Command))

