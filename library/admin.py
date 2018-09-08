from django.contrib import admin
from .models import Language, ProgrammingLanguage, Profession, Module, Class, Category, ExternalModule, Command, Call, Word, Combo

admin.site.register((Language, ProgrammingLanguage, Profession, Module, Class, Category, ExternalModule, Command, Call, Word, Combo))

