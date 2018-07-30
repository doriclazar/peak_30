from django.contrib import admin
from .models import Profession, Module, Category, ExternalModule, Command, Call, Word, Combo

admin.site.register((Profession, Module, Category, ExternalModule, Command, Call, Word, Combo))

