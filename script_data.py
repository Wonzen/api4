import psycopg2
from user_data import date_birthday, name_first, name_last, gen, path_avatar, res_address_street_name, \
    res_address_street_num, view_phone,number_phone, view_email, email
#id_user 1 нужен цикл

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
            """insert into users (id, full_name, gender, date_birthday, path_avatar, residential_address) values \
            (%s, %s, %s, %s, %s, %s);""", (1, name_first + ' ' + name_last, gen, date_birthday, path_avatar, res_address_street_name+' '+res_address_street_num)
        )
    with connection.cursor() as cursor:

        cursor.execute(
            """insert into phones (id_user, view_phone, number_phone) values \
            (%s, %s, %s);""", (1, view_phone, number_phone)
        )

    with connection.cursor() as cursor:

        cursor.execute(
            """insert into email (id_user, view_email, email) values \
            (%s, %s, %s);""", (1, view_email, email)
        )




except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print('[INFO] PostgreSQL connection close')