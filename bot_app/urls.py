from django.urls import path
from . import views

urlpatterns = [
    path('information/', views.UserInfo.as_view(), name='user_information'),
    path('send_msg/<int:num_msg>', views.SendMessage.as_view(), name='send_message'),
    path('send_msg_now/<int:num_msg>', views.SendMessageNow.as_view(), name='send_message_now'),
]
