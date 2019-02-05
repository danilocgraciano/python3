from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_mysqldb import MySQL

from game import Game
from user import User

from game_dao import GameDao
from user_dao import UserDao

app = Flask(__name__)
app.secret_key = "mK6W8Vhu7qQCb6hV"

app.config['MYSQL_HOST'] = "127.0.0.1"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "root"
app.config['MYSQL_DB'] = "playstore"
app.config['MYSQL_PORT'] = 3306

db = MySQL(app)

gameDao = GameDao(db)
userDao = UserDao(db)

@app.route("/")
def home():
    games = gameDao.read()
    return render_template(
        "game/list.html",
        title="Games",
        list=games
    )

@app.route("/new")
def new():
    if (not is_logged_in()):
        return redirect(url_for("login", url_after_login=url_for("new")))

    game = Game(None, None, None)

    return render_template(
        "game/form.html",
        title="New Game",
        action=url_for("save"),
        game=game
    )

@app.route("/edit/<int:id>")
def edit(id):
    if (not is_logged_in()):
        return redirect(url_for("login", url_after_login=url_for("edit")))

    game = gameDao.read_by_id(id)

    return render_template(
        "game/form.html",
        title="New Game",
        action=url_for("save"),
        game=game
    )

@app.route("/delete/<int:id>")
def delete(id):
    gameDao.delete(id)
    flash("Game deleted!")
    return redirect(url_for("home"))


@app.route("/save", methods=["POST"])
def save():
    name = request.form['name']
    category = request.form['category']
    device = request.form['device']
    id = request.form['id']
    game = Game(name, category, device, id)
    gameDao.save(game)
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

    user = userDao.read_by_id(username)

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

#app.run(host='0.0.0.0', port=8080)
app.run(debug=True)