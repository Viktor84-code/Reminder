# Habit Tracker (Reminder)

Трекер полезных привычек. Полноценное SPA-приложение с бэкендом на Django + DRF и фронтендом на Vue 3.

---

## 🌐 Демо

Проект доступен по адресу:  
**[http://93.77.161.31:3001](http://93.77.161.31:3001)**

---

## 🧰 Технологии

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

---

## 📦 Установка и запуск

### Бэкенд

1. Клонировать репозиторий:
```bash
git clone https://github.com/Viktor84-code/Reminder.git
cd Reminder
```
Создать виртуальное окружение и установить зависимости:

```bash
python -m venv venv
venv\Scripts\activate  # или source venv/bin/activate
pip install -r requirements.txt
```
Создать файл .env по примеру .env.template

Применить миграции:

```bash
python manage.py migrate
```
Запустить бэкенд:

```bash
python manage.py runserver
```
Фронтенд
Перейти в папку frontend:

```bash
cd frontend
npm install
npm run dev
```
🐳 Запуск через Docker
1. Подготовка
Убедитесь, что Docker и Docker Compose установлены.

2. Настройка переменных окружения
Скопируйте .env.template в .env и заполните значения:

```bash
cp .env.template .env
```
3. Сборка и запуск
```bash
docker-compose up -d --build
```
4. Доступ
Фронтенд: http://localhost:3000

API: http://localhost:8000/api/

Swagger: http://localhost:8000/api/docs/

Админка: http://localhost:8000/admin

5. Остановка
```bash
docker-compose down
```
📚 Документация API
Swagger доступен по адресу:
http://localhost:8000/api/docs/

🧪 Тесты
```bash
python manage.py test
```
Покрытие: 93%

🤖 Telegram
Для работы бота добавьте в .env:

env
TG_BOT_TOKEN=your_token
Бот отправляет напоминания о привычках в указанное время.

🔧 CI/CD
При каждом пуше в ветку feature/docker-compose запускается GitHub Actions:

Линтинг (flake8)

Тесты (python manage.py test)

Сборка Docker-образов

Автоматический деплой на сервер

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