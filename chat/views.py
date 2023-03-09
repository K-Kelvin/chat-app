from django.shortcuts import render

def index(request):
    ''' Initial page of the chat app'''
    return render(request, "chat/index.html")

def room(request, room_name):
    ''' Render chat room UI and logic'''
    return render(request, "chat/chat.html", {"room_name": room_name})
