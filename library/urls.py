from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='get_library'),

    #contain list of bots. Update to contain list of modules too.
    url(r'^professions/$', views.get_professions, name='get_professions'),
    #GET COMMANDS SEPARATED BY LIVE-LINK MODULES
    url(r'^modules/$', views.get_modules, name='get_modules'),
    #GET COMMANDS SEPARATED BY LIVE-LINK CATEGORIES
    url(r'^categories/$', views.get_categories, name='get_categories'),
    #GET ALL COMMANDS - SORT BY NAME OR POPULARITY
    url(r'^commands/$', views.get_commands, name='get_commands'),

    url(r'^professions/(?P<profession_code>.+)/update/$', views.update_profession, name='update_profession'),
    url(r'^professions/(?P<profession_code>.+)/$', views.get_profession, name='get_profession'),
    url(r'^modules/(?P<module_code>.+)/$', views.get_module, name='get_module'),
    url(r'^categories/(?P<category_code>.+)/$', views.get_category, name='get_category'),
    url(r'^commands/(?P<command_code>.+)/download/$', views.download_command, name='download_command'),
    url(r'^commands/(?P<command_code>.+)/$', views.get_command, name='get_command'),
]
