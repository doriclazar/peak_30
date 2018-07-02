from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='get_profiles'),

    url(r'^users/$', views.get_users, name='get_users'),
    url(r'^groups/$', views.get_groups, name='get_groups'),
    url(r'^professions/$', views.get_professions, name='get_professions'),
    url(r'^bots/$', views.get_bots, name='get_bots'),

    url(r'^user/(?P<username>.+)/$', views.get_user_profile, name='get_user_profile'),
    url(r'^group/(?P<group_name>.+)/$', views.get_group_profile, name='get_group_profile'),
    url(r'^profession/(?P<profession_code>.+)/$', views.get_profession_profile, name='get_profession_profile'),
    url(r'^bot/(?P<bot_code>.+)/$', views.get_bot_profile, name='get_bot_profile'),
]
