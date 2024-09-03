# Используем официальный образ Python
FROM python:3.8-slim

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y gcc libffi-dev libssl-dev

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл с зависимостями в контейнер
COPY requirements.txt requirements.txt

# Обновляем pip и устанавливаем зависимости
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . .

# Определяем команду для запуска бота
CMD ["python", "bot.py"]
