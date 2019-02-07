from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from app.route import error, game, user

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    db.init_app(app)

    app.register_blueprint(error)
    app.register_blueprint(game)
    app.register_blueprint(user)

    return app