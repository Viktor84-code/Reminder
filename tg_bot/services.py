import requests
from django.conf import settings


def send_telegram_message(chat_id, message):
    """Отправка сообщения в Telegram"""
    url = f"https://api.telegram.org/bot{settings.TG_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": message, "parse_mode": "HTML"}
    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        return True
    except Exception as e:
        print(f"Telegram error: {e}")
        return False
