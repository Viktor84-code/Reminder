from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    telegram_chat_id = models.CharField(max_length=100, blank=True, null=True, verbose_name="Telegram ID")

    def __str__(self):
        return f"{self.user.username} - {self.telegram_chat_id}"
