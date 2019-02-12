from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()

from app.route import book, error

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(book, url_prefix='/api')
    app.register_blueprint(error)


    return app