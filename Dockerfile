# Используем официальный образ Python
FROM python:3.9-slim

ENV key='7832827756:AAHlvomwWxVVu3vK83q1FFjXl_NOadjt8aU'

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код бота
COPY . /app/


    

# Запускаем бота
CMD ["python", "botyara.py"]