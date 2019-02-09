from flask import redirect, url_for
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash

from app import db, create_app
from app.model import Game, User, Category

app = create_app()
migrate = Migrate(app, db)

@app.route("/init")
def init_data():

    #db.drop_all()
    #db.create_all()

    kids = Category(None,"Kids")
    db.session.add(kids)
    db.session.commit()

    db.session.add(Game(None, "Pou", kids, "Moto G2"))
    db.session.add(Game(None, "Subway Surfers", kids, "Moto G3"))
    db.session.add(Game(None, "My Talking Tom", kids, "Moto G3"))
    db.session.add(Game(None, "Despicable Me", kids, "iPhone"))
    db.session.add(Game(None, "Zombie Tsunami", kids, "iPhone"))
    db.session.commit()

    db.session.add(User(None, "danilocgraciano", generate_password_hash("123456")))
    db.session.commit()

    return redirect(url_for("game.home"))

if (__name__ == "__main__"):
    # app.run(host='0.0.0.0', port=8080)
    app.run(debug=True)