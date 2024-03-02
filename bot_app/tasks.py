import random, time, telebot, os
from .models import TelegramUser, MessageInfo
from celery import shared_task

TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)


@shared_task
def send_message_to_all_task(num_msg):
    users = TelegramUser.objects.all()

    for user in users:
        message_failed = random.sample(range(num_msg), 2)
        num_sent = 0
        num_failed = 0
        for i in range(num_msg):
            if i not in message_failed:
                message = f"سلام {user.first_name} عزیز! -{i}"
                time.sleep(0.5)
                bot.send_message(chat_id=user.telegram_id, text=message)
                num_sent += 1
            else:
                time.sleep(0.5)
                num_failed += 1

        MessageInfo.objects.create(telegram_user=user,
                                   success_msg=num_sent,
                                   fail_msg=num_failed)
