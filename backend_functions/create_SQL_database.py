import sqlite3
from backend_functions.collect_data import collect_data
import os

def create_SQL_database():
    # Проверка наличия базы данных и создание, если необходимо
    if not os.path.exists('data/database.db'):
        conn = sqlite3.connect('data/database.db')
        cursor = conn.cursor()

        # Создание таблицы
        create_table_query = '''
        CREATE TABLE products (
            product_name TEXT PRIMARY KEY,
            product_price integer,
            product_mobile_internet integer,
            product_TV integer,
            product_internet_speed integer,
            product_minutes integer
        );
        '''
        cursor.execute(create_table_query)

        # Сохранение изменений и закрытие соединения
        conn.commit()
        conn.close()

    # Подключение к базе данных
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()

    delete_query = '''
    DELETE FROM products
    '''
    cursor.execute(delete_query)

    # Словарь с данными
    data = collect_data()

    # Добавление данных в таблицу
    for product, product_data in data.items():
        insert_query = '''
        INSERT INTO products (product_name, product_price, product_mobile_internet, product_TV, product_internet_speed, product_minutes)
        VALUES (?, ?, ?, ?, ?, ?)
        '''
        values = (
            product,
            product_data.get('product_price'),
            product_data.get('product_mobile_internet'),
            product_data.get('product_TV'),
            product_data.get('product_internet_speed'),
            product_data.get('product_minutes')
        )
        cursor.execute(insert_query, values)

    # Сохранение изменений и закрытие соединения
    conn.commit()
    select_query = '''
    SELECT * FROM products
    '''
    cursor.execute(select_query)
    print(cursor.fetchall())

    conn.close()