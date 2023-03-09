from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message, Room

@login_required
def index(request):
    ''' Initial page of the chat app'''
    print(Room)
    users = User.objects.all().exclude(username=request.user) # other users except the current user
    return render(request, "chat/chat.html", {
        "users": users,
    })

@login_required
def room(request, room_name):
    ''' Render chat room UI and logic'''
    users = User.objects.all().exclude(username=request.user) # other users except the current user

    sender = request.user
    recipient = get_object_or_404(User, username=room_name)

    if (request.method == 'POST'):
        message = request.POST.get("message")
        if message:
            Message.objects.create(sender=sender, recipient=recipient, message=message)

    messages = Message.get_all_messages(id_1=sender.id, id_2=recipient.id)
    
    return render(request, "chat/chat.html", {
        "room_name": room_name,
        "users": users,
        "messages": messages,
        "recipient": recipient,
    })
