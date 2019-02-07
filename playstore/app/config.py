import os

SECRET_KEY = "mK6W8Vhu7qQCb6hV"

SQLALCHEMY_DATABASE_URI = os.environ.get('HOSTNAME') or "postgresql://postgres:postgres@localhost:5432/playstore"
SQLALCHEMY_TRACK_MODIFICATIONS = False


MYSQL_HOST = "127.0.0.1"
MYSQL_USER = "root"
MYSQL_PASSWORD = "root"
MYSQL_DB = "playstore"
MYSQL_PORT = 3306