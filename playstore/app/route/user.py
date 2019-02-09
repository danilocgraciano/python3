from functools import wraps

from flask import Blueprint, render_template, request, redirect, session, flash, url_for, g

from app import db
from app.model import User

user = Blueprint("user",__name__)


@user.route("/login")
def login():
    url_after_login = request.args.get('url_after_login')
    return render_template(
        "login.html",
        title="Login",
        url_after_login=url_after_login
    )

@user.route("/logout")
def logout():
    session.clear()
    flash("Logout successfully!")
    return redirect(url_for("game.home"))

@user.route("/authenticate", methods=["POST"])
def authenticate():

    username = request.form["username"]
    password = request.form["password"]
    url_after_login = request.form["url_after_login"]

    user = db.session.query(User).filter(User.name == username, User.password == password).all()

    if (len(user) > 0):
        user = user[0]
        if (password == user.password ):
            session["logged_user"] = username
            flash(f"{user.name} logged in!")
            return redirect(url_after_login)
    else:
        flash("Invalid login, try again!")
        return redirect(url_for("user.login", url_after_login=url_after_login))

@user.before_app_request
def load_logged_user():
    if ("logged_user" not in session or session["logged_user"] == None):
        g.user = None
    else:
        g.user = session["logged_user"]

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('user.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function