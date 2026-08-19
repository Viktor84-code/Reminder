# Базовый образ с Python 3.13
FROM python:3.13-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем системные зависимости для PostgreSQL и Redis
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Копируем файл с зависимостями
COPY requirements.prod.txt .

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.prod.txt


# Копируем весь проект
COPY . .

# Создаём директории для статики и медиа
RUN mkdir -p /app/static /app/media

# Открываем порт 8000
EXPOSE 8000

# Команда для запуска (переопределяется в docker-compose)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
