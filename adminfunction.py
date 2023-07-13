import psycopg2

# Параметры подключения к базе данных

# Установка соединения
conn = psycopg2.connect(
    host="127.0.0.1",
    port="5432",
    database="admin_database",
    user="oleg",
    password="Zxcv7890"
)
cursor = conn.cursor()
username = "Admin"
password = "Qwerty123@"

sql = f"INSERT INTO admins (username, password) VALUES ('{username}', '{password}')"
# Выполнение SQL-запроса
cursor.execute(sql)

# Применение изменений
conn.commit()
cursor.close()

# Закрытие соединения
conn.close()