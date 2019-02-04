from flask import Flask, render_template, request, redirect, session, flash, url_for
from game import Game
from user import User

games = []
pou = Game("pou", "Kids", "Moto G2")
subway_surfers = Game("subway surfers", "Kids", "Moto G3")
my_talking_tom = Game("Mm talking tom", "Kids", "Moto G3")
despicable_me = Game("despicable me", "Kids", "iPhone")
zombie_tsunami = Game("zombie tsunami", "Kids", "iPhone")

games.append(pou)
games.append(subway_surfers)
games.append(my_talking_tom)
games.append(despicable_me)
games.append(zombie_tsunami)

user1 = User("danilocgraciano","Danilo C. Graciano","123456")
users = {user1.id : user1}

app = Flask(__name__)
app.secret_key = "mK6W8Vhu7qQCb6hV"

@app.route("/")
def home():
    return render_template(
        "list.html",
        title="Games",
        list=games
    )

@app.route("/new")
def new():
    if (not is_logged_in()):
        return redirect(url_for("login", url_after_login=url_for("new")))

    return render_template(
        "form.html",
        title="New Game"
    )

@app.route("/create", methods=["POST"])
def create():
    name = request.form['name']
    category = request.form['category']
    device = request.form['device']
    game = Game(name, category, device)
    games.append(game)
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

    user = users[username]

    if (user is not None and (username == user.id and password == user.password) ):
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