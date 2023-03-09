from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def index(request):
    ''' Initial page of the chat app'''
    users = User.objects.all().exclude(username=request.user) # other users except the current user
    return render(request, "chat/chat.html", {
        "users": users,
    })

def room(request, room_name):
    ''' Render chat room UI and logic'''
    users = User.objects.all().exclude(username=request.user) # other users except the current user
    return render(request, "chat/chat.html", {
        "room_name": room_name,
        "users": users,
    })
