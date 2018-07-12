from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='get_profiles'),

    url(r'^users/$', views.get_users, name='get_users'),
    url(r'^groups/$', views.get_groups, name='get_groups'),
    #MOVED TO INDEX OF professions app
    #url(r'^professions/$', views.get_professions, name='get_professions'),
    url(r'^bots/$', views.get_bots, name='get_bots'),

    url(r'^groups/(?P<group_name>.+)/$', views.get_group_profile, name='get_group_profile'),
    url(r'^users/(?P<username>.+)/$', views.get_user_profile, name='get_user_profile'),
    url(r'^bots/(?P<bot_code>.+)/$', views.get_bot_profile, name='get_bot_profile'),
]
