from django.shortcuts import render
from .models import TelegramUser, NormalUser
from .serializers import TelegramUserSerializer, NormalUserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from datetime import datetime
import pytz
from .tasks import send_message_to_all_task


class UserInfo(APIView):
    @csrf_exempt
    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        telegram_username = request.POST.get('telegram_username')
        telegram_id = request.POST.get('telegram_id')

        check_exist_normal_user = NormalUser.objects.filter(telegram_id=telegram_id).exists()
        if check_exist_normal_user:
            serializer = NormalUserSerializer(check_exist_normal_user)
            return Response(serializer.data, status.HTTP_200_OK)

        check_exist_telegram_user = TelegramUser.objects.filter(telegram_id=telegram_id).exists()
        if check_exist_telegram_user:
            serializer = TelegramUserSerializer(check_exist_telegram_user)
            return Response(serializer.data, status.HTTP_200_OK)

        TelegramUser.objects.create(first_name=first_name,
                                    last_name=last_name,
                                    telegram_username=telegram_username,
                                    telegram_id=telegram_id)

        new_telegram_user = TelegramUser.objects.get(telegram_id=telegram_id)
        serializer = TelegramUserSerializer(new_telegram_user)
        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request):
        return Response(status=status.HTTP_400_BAD_REQUEST)


def time_set():
    _datetime = datetime.now()
    return datetime(year=_datetime.year, month=_datetime.month, day=_datetime.day, hour=_datetime.hour, minute=24)


class SendMessage(APIView):
    def get(self, request, num_msg):
        local_timezone = pytz.timezone('Asia/Tehran')
        eta_time = datetime.now(local_timezone).replace(year=time_set().year,
                                                        month=time_set().month,
                                                        day=time_set().day,
                                                        hour=time_set().hour,
                                                        minute=time_set().minute)
        send_message_to_all_task.apply_async(args=(num_msg,), eta=eta_time)
        return Response(None, status=status.HTTP_200_OK)


class SendMessageNow(APIView):
    def get(self, request, num_msg):
        send_message_to_all_task.delay(num_msg)
        return Response(None, status=status.HTTP_200_OK)