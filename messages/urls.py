from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #url(r'^/$', views.get_messages, name='get_messages'),

   # url(r'^inbox/(?P<message_code>.+)/$', views.get_inbox_message, name='get_inbox_message'),
    #url(r'^outbox/(?P<message_code>.+)/$', views.get_outbox_message, name='get_outbox_message'),
]
