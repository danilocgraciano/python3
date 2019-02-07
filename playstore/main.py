from flask import redirect, url_for
from app import db, create_app
from app.model import Game, User

app = create_app()

@app.route("/init")
def init_data():
    db.drop_all()
    db.create_all()

    db.session.add(Game(None, "pou", "kids", "Moto G2"))
    db.session.add(Game(None, "subway surfers", "kids", "Moto G3"))
    db.session.add(Game(None, "my talking tom", "kids", "Moto G3"))
    db.session.add(Game(None, "despicable me", "kids", "iPhone"))
    db.session.add(Game(None, "zombie tsunami", "kids", "iPhone"))
    db.session.commit()

    db.session.add(User(None, "danilocgraciano","123456"))
    db.session.commit()

    return redirect(url_for("game.home"))

if (__name__ == "__main__"):
    # app.run(host='0.0.0.0', port=8080)
    app.run(debug=True)