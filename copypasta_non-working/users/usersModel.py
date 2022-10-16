from copypasta.db import post_connection
from copypasta.users.entites import Users


class UserModel():
    @classmethod
    def post_users(self):
        try:
            connection = post_connection()
            users = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT idd, full_name, gender, date_birthday, path_avatar, residential_address FROM "
                               "users ORDER BY full_name ASC")
                resultset = cursor.fetchall()
                for row in resultset:
                    user = Users(row[0], row[1], row[2], row[3], row[4], row[5])
                    users.append(user.to_Json())
            connection.close()
            return users
        except Exception as ex:
            raise Exception(ex)
