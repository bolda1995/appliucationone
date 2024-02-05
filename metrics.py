from prometheus_client import Gauge
import time

# Создаем метрику Gauge для отслеживания времени работы приложения
app_uptime = Gauge('app_uptime_seconds', 'Time since the application started')

# Запоминаем время старта приложения
start_time = time.time()

def update_uptime():
    # Обновляем метрику на текущее время минус время старта
    current_time = time.time()
    app_uptime.set(current_time - start_time)
