from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='get_library'),

    url(r'^professions/$', views.get_professions, name='get_professions'),
    url(r'^modules/$', views.get_modules, name='get_modules'),
    url(r'^categories/$', views.get_categories, name='get_categories'),
    url(r'^commands/$', views.get_commands, name='get_commands'),


    url(r'^commands/new_command/$', views.new_command, name='new_command'),
    url(r'^commands/search_all/$', views.search_all, name='search_all'),

    url(r'^professions/(?P<profession_code>.+)/update/$', views.update_profession, name='update_profession'),
    url(r'^professions/(?P<profession_code>.+)/$', views.get_profession, name='get_profession'),
    url(r'^modules/(?P<module_code>.+)/$', views.get_module, name='get_module'),
    url(r'^categories/(?P<category_code>.+)/$', views.get_category, name='get_category'),
    url(r'^commands/(?P<command_code>.+)/download/$', views.download_command, name='download_command'),
    url(r'^commands/(?P<command_code>.+)/$', views.get_command, name='get_command'),
    
    url(r'^commands/new_command/ajax/get_classes$', views.get_classes, name='get_classes'),
]
