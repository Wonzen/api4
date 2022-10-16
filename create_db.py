import psycopg2

try:
    connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='VbrrbVf',
        database='postgres'
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE DATABASE add;"""
        )
        print(f"База данных создана")
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print('[INFO] PostgreSQL connection close')

try:
    connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='VbrrbVf',
        database='add'
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute(

            """CREATE TABLE users(
            id serial PRIMARY KEY,
            full_name varchar(255),
            gender varchar(6),
            date_birthday varchar(50),
            path_avatar varchar(255),
            residential_address text);"""
        )
        print(f"Таблица users создана")
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE phones(
            id_user integer references users(id),
            view_phone varchar(20),
            number_phone varchar(20));"""
        )
        print(f"Таблица phones создана")
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE email(
            id_user integer references users(id),
            view_email varchar(20),
            email varchar(100));"""
        )
        print(f"Таблица email создана")
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print('[INFO] PostgreSQL connection close')
