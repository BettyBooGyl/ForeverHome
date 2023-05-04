from django.shortcuts import render
from django.contrib.auth import get_user_model
from messaging_app.models import Message

User = get_user_model()

def messages(request, id1, id2):
    if (User.objects.get(userID=id1) == request.user):
        user_obj = User.objects.get(userID=id2)
    else:
        user_obj = User.objects.get(userID=id1)
    users = User.objects.exclude(username=request.user.username)

    thread_name = f'chat_{id1}{id2}'
    message_obj = Message.objects.filter(thread_name=thread_name)
    return render(request, 'messaging_page.html', context={'users':users, 'user':user_obj, 'messages': message_obj})