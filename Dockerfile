# Используйте конкретную минорную версию Python
FROM python:3.12

# Установите рабочий каталог в контейнере
WORKDIR /app

# Сначала копируем только файл requirements.txt для кэширования слоев
COPY requirements.txt .

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.txt

# Копируем оставшиеся файлы проекта
COPY . .

# Создаем пользователя для запуска приложения
RUN useradd appuser && chown -R appuser /app
USER appuser

# Открываем порт 8000
EXPOSE 8000

# Запускаем приложение
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
