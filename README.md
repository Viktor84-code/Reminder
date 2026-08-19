# Habit Tracker

Трекер полезных привычек. Полноценное SPA-приложение с бэкендом на Django + DRF и фронтендом на Vue 3.

## 📋 Описание

Приложение для отслеживания привычек с интеграцией Telegram-бота, Celery для фоновых задач и современным интерфейсом.

## 🚀 Технологии

### Бэкенд
- Python 3.13
- Django 6.0
- Django REST Framework
- JWT авторизация
- PostgreSQL
- Redis
- Celery + Beat
- Telegram Bot API
- Swagger (drf-spectacular)
- Docker

### Фронтенд
- Vue 3
- Vite
- Vue Router
- Axios
- CSS

## 📦 Установка и запуск

### Бэкенд

1. Клонировать репозиторий:
```bash
git clone git@github.com:Viktor84-code/habit-tracker.git
cd habit-tracker
Создать виртуальное окружение и установить зависимости:

bash
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate
pip install -r requirements.txt
Создать файл .env по примеру .env.example

Запустить Docker-контейнеры (если остановлены):

bash
docker start habits-postgres
docker start habit-redis
Применить миграции:

bash
python manage.py migrate
Запустить бэкенд:

bash
python manage.py runserver
(Опционально) Запустить Celery:

bash
celery -A config worker --loglevel=info -P eventlet
celery -A config beat --loglevel=info
```
Фронтенд
Перейти в папку frontend:
```
bash
cd frontend
Установить зависимости:

bash
npm install
Запустить dev-сервер:

bash
npm run dev
📚 Документация API
Swagger доступен по адресу:

text
http://127.0.0.1:8000/api/docs/
🧪 Тесты
bash
python manage.py test
Покрытие: 93%
```

🤖 Telegram
Для работы бота добавьте в .env:

text
TG_BOT_TOKEN=your_token
Бот отправляет напоминания о привычках в указанное время.

📱 Интерфейс
Регистрация / Логин

Список привычек (с пагинацией)

Создание привычки

Редактирование привычки

Удаление привычки

Публичные привычки

👤 Автор
Виктор Бриткин
GitHub: Viktor84-code

## 🐳 Запуск через Docker

### 1. Настроить переменные окружения

```bash
cp .env.example .env
```
Отредактируй .env под свои данные.

2. Запустить все сервисы
```bash
docker-compose up -d --build
```
3. Проверить, что всё работает
Бэкенд: http://localhost:8000

Swagger: http://localhost:8000/api/docs/

Фронтенд: http://localhost:3000

4. Остановка
```bash
docker-compose down
```