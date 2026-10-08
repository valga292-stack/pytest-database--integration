import psycopg2
import pytest


def test_postgresql_connection_and_data():
    # 1. Подключаемся к нашему работающему Docker-контейнеру базы данных
    connection = psycopg2.connect(
        host="localhost",
        database="enterprise_telecom_db",
        user="qa_valery",
        password="secret_password123",
        port="5432"
    )

    # 2. Создаем курсор для выполнения SQL-запросов
    cursor = connection.cursor()

    # 3. Проверяем связь — запрашиваем данные из нашей таблицы telecom_users
    cursor.execute("SELECT * FROM telecom_users;")
    rows = cursor.fetchall()

    # 4. Выводим информацию о записях прямо в лог прогона
    print(f"\n[INFO] Connected to PostgreSQL! Total records found in DB: {len(rows)}")

    # 5. QA-проверка (Assert): проверяем, что таблица содержит данные
    assert len(rows) > 0, "Error: The telecom_users table is empty!"

    # 6. Закрываем соединения
    cursor.close()
    connection.close()
