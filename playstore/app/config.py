import os

SECRET_KEY = os.environ.get('SECRET_KEY') or "mK6W8Vhu7qQCb6hV"

SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or "postgresql://postgres:postgres@localhost:5432/playstore"
SQLALCHEMY_TRACK_MODIFICATIONS = False