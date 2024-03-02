from django.db import models


class TelegramUser(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    telegram_username = models.CharField(max_length=255, null=True, blank=True)
    telegram_id = models.PositiveBigIntegerField(null=True, blank=True, unique=True)


class MessageInfo(models.Model):
    telegram_user = models.ForeignKey('TelegramUser', on_delete=models.CASCADE)
    success_msg = models.PositiveIntegerField(null=True, blank=True)
    fail_msg = models.PositiveIntegerField(null=True, blank=True)


class NormalUser(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    telegram_username = models.CharField(max_length=255, null=True, blank=True)
    telegram_id = models.PositiveBigIntegerField(null=True, blank=True, unique=True)
