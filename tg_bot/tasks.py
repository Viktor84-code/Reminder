from celery import shared_task
from django.utils import timezone

from habits.models import Habit

from .services import send_telegram_message


@shared_task
def send_habit_reminders():
    """Отправка напоминаний о привычках"""
    now = timezone.now()
    current_time = now.time()

    habits = Habit.objects.filter(
        time__hour=current_time.hour, time__minute=current_time.minute
    )

    for habit in habits:
        chat_id = habit.user.profile.telegram_chat_id
        if chat_id:
            message = f"🔔 Напоминание: {habit.action} в {habit.place} в {habit.time}"
            send_telegram_message(chat_id, message)
