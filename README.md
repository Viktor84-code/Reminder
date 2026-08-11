# Habit Tracker

Трекер полезных привычек. Курсовая работа Skypro.

## 📋 Описание

Бэкенд-часть SPA-приложения для отслеживания привычек. Реализована на Django + DRF с интеграцией Telegram-бота и Celery для напоминаний.

## 🚀 Технологии

- Python 3.13
- Django 6.0
- Django REST Framework
- JWT авторизация
- PostgreSQL
- Redis
- Celery
- Telegram Bot API
- Swagger (drf-spectacular)
- Docker

## 📦 Установка

1. Клонировать репозиторий:
```bash
git clone git@github.com:Viktor84-code/habit-tracker.git
cd habit-tracker
Создать виртуальное окружение:

bash
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate для Windows
Установить зависимости:

bash
pip install -r requirements.txt
Создать файл .env (по примеру .env.template)

Запустить Docker-контейнеры:

bash
docker run -d --name habits-postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=habits -p 5433:5432 postgres:15
docker run -d --name habit-redis -p 6379:6379 redis:7
Применить миграции:

bash
python manage.py migrate
Запустить сервер:

bash
python manage.py runserver
🔧 Запуск Celery
В отдельных терминалах:

bash
celery -A config worker --loglevel=info -P eventlet
celery -A config beat --loglevel=info
📚 Документация API
Swagger доступен по адресу:
```
text
http://127.0.0.1:8000/api/docs/
🧪 Тесты
```bash
python manage.py test
Покрытие: 93%
```
🤖 Telegram
Для работы бота добавьте в .env:

text
TG_BOT_TOKEN=your_token
Бот отправляет напоминания о привычках в указанное время.

👤 Автор
Viktor Britkin