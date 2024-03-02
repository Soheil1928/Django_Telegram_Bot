from rest_framework import serializers
from .models import TelegramUser, NormalUser


class NormalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NormalUser
        fields = ['id', 'first_name', 'last_name', 'telegram_username', 'telegram_id']


class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = ['id', 'first_name', 'last_name', 'telegram_username', 'telegram_id']