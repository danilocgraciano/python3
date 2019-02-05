from game import Game

SQL_CREATE_GAME = 'INSERT into game (name, category, device) values (%s, %s, %s)'
SQL_UPDATE_GAME = "UPDATE game SET name=%s, category=%s, device=%s where id = %s"
SQL_READ_GAMES = 'SELECT id, name, category, device from game'
SQL_READ_BY_ID = 'SELECT id, name, category, device from game where id = %s'
SQL_DELETE_GAME = 'delete from game where id = %s'

class GameDao:
    def __init__(self, db):
        self.__db = db

    def save(self, game):
        cursor = self.__db.connection.cursor()

        if (game.id):
            cursor.execute(SQL_UPDATE_GAME, (game.name, game.category, game.device, game.id))
        else:
            cursor.execute(SQL_CREATE_GAME, (game.name, game.category, game.device))
            game.id = cursor.lastrowid
        self.__db.connection.commit()
        return game

    def read(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_READ_GAMES)
        games = cursor.fetchall()
        return map_games(games)

    def read_by_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_READ_BY_ID, (id,))
        row = cursor.fetchone()
        return Game(row[1], row[2], row[3], id=row[0])

    def delete(self, id):
        self.__db.connection.cursor().execute(SQL_DELETE_GAME, (id, ))
        self.__db.connection.commit()

def map_games(rows):
    def create_game_by_row(row):
        return Game(row[1], row[2], row[3], id=row[0])
    return list(map(create_game_by_row, rows))