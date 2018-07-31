from django.contrib import admin
from .models import Language, Profession, Module, Category, ExternalModule, Command, Call, Word, Combo

admin.site.register((Language, Profession, Module, Category, ExternalModule, Command, Call, Word, Combo))

