from django.urls import path
from messaging_app import views

urlpatterns = [
    path('messages/<str:id1><str:id2>', views.messages, name='messages'),
]