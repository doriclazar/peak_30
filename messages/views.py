from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .models import Message, CarbonCopy

def get_messages(request, **kwargs):
    kwargs['user_inbox'] = Message.objects.filter(user = request.user)
    kwargs['user_cc'] = CarbonCopy.objects.filter(user = request.user)
    kwargs['user_outbox'] = Message.objects.filter(creator = request.user)
    return render(request, 'messages/index.html', kwargs)


def get_message(request, **kwargs):
    return render(request, 'messages/index.html', kwargs)

