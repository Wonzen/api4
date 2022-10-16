import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='VbrrbVf',
        database='add',

    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute(
            '''select * from users;'''
        )
        results_full = cursor.fetchall()


    with connection.cursor() as cursor:
        cursor.execute(
            '''select full_name from users;'''
        )
        results_name = cursor.fetchall()

    with connection.cursor() as cursor:
        cursor.execute(
            '''select gender from users;'''
        )
        results_gender = cursor.fetchall()

    with connection.cursor() as cursor:
        cursor.execute(
            '''select path_avatar from users;'''
        )
        results_path_avatar = cursor.fetchall()
    with connection.cursor() as cursor:
        cursor.execute(
            '''select residential_address from users;'''
        )
        results_residential_address = cursor.fetchall()



except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")

