from user import User

SQL_READ_BY_ID = 'SELECT id, name, password from user where id = %s'

class UserDao:
    def __init__(self, db):
        self.__db = db

    def read_by_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_READ_BY_ID, (id,))
        data = cursor.fetchone()
        user = map_user(data) if data else None
        return user

def map_user(row):
    return User(row[0], row[1], row[2])