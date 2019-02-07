from flask import render_template, request, redirect, session, flash, url_for

from app.model import Game
from app.model import User

from app import create_app
from app import db

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

    return redirect(url_for("home"))

@app.route("/")
def home():
    games = db.session.query(Game)
    return render_template(
        "game/list.html",
        title="Games",
        list=games
    )

@app.route("/new")
def new():
    if (not is_logged_in()):
        return redirect(url_for("login", url_after_login=url_for("new")))

    game = Game(None, None, None, None)

    return render_template(
        "game/form.html",
        title="New Game",
        action=url_for("save"),
        game=game
    )

@app.route("/edit/<int:id>")
def edit(id):
    if (not is_logged_in()):
        return redirect(url_for("login", url_after_login=url_for("edit",id=id)))

    game = db.session.query(Game).get(id)

    return render_template(
        "game/form.html",
        title="Edit Game",
        action=url_for("save"),
        game=game
    )

@app.route("/delete/<int:id>")
def delete(id):
    db.session.query(Game).filter(Game.id == id).delete()
    db.session.commit()
    flash("Game deleted!")
    return redirect(url_for("home"))


@app.route("/save", methods=["POST"])
def save():

    id = request.form['id'] or None
    name = request.form['name']
    category = request.form['category']
    device = request.form['device']
    game = Game(id, name, category, device)
    db.session.merge(game)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/login")
def login():
    url_after_login = request.args.get('url_after_login')
    return render_template(
        "login.html",
        title="Login",
        url_after_login=url_after_login
    )

@app.route("/logout")
def logout():
    session["logged_user"] = None
    flash("Logout successfully!")
    return redirect(url_for("home"))

@app.route("/authenticate", methods=["POST"])
def authenticate():

    username = request.form["username"]
    password = request.form["password"]
    url_after_login = request.form["url_after_login"]

    user = None

    if (user):
        if (password == user.password ):
            session["logged_user"] = username
            flash(f"{user.name} logged in!")
            return redirect(url_after_login)
    else:
        flash("Invalid login, try again!")
        return redirect(url_for("login"))

def is_logged_in():
    if ("logged_user" not in session or session["logged_user"] == None):
        return False
    return True


if (__name__ == "__main__"):
    # app.run(host='0.0.0.0', port=8080)
    app.run(debug=True)