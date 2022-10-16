import psycopg2
from psycopg2 import DatabaseError
import config_db


def post_connection():
    try:
        return psycopg2.connect(
            host=config_db.host,
            user=config_db.user,
            password=config_db.password,
            database=config_db.database,

        )
    except DatabaseError as ex:
        raise ex
