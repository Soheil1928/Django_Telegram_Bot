from django.contrib import admin
from .models import TelegramUser, NormalUser, MessageInfo


@admin.register(NormalUser)
class NormalUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name']


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name']


@admin.register(MessageInfo)
class MessageInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'telegram_user']