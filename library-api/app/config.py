import os

SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or "postgresql://postgres:postgres@localhost:5432/library"
SQLALCHEMY_TRACK_MODIFICATIONS = False