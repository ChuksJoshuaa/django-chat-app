
from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('chat/', views.chat_view, name='chats'),
    path('chat/<int:sender>/<int:receiver>/', views.message_view, name='chat'),
    path('api/messages/<int:sender>/<int:receiver>/', views.my_message, name='message-detail'),
    path('api/messages/', views.my_message, name='message-list'),
]
