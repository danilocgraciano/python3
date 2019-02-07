from flask import Blueprint, render_template, request, redirect, session, flash, url_for

from app import db
from app.model import Game

game = Blueprint("game",__name__)

@game.route("/")
def home():
    games = db.session.query(Game)
    return render_template(
        "game/list.html",
        title="Games",
        list=games
    )

@game.route("/new")
def new():
    if (not is_logged_in()):
        return redirect(url_for("user.login", url_after_login=url_for("game.new")))

    game = Game(None, None, None, None)

    return render_template(
        "game/form.html",
        title="New Game",
        action=url_for("game.save"),
        game=game
    )

@game.route("/edit/<int:id>")
def edit(id):
    if (not is_logged_in()):
        return redirect(url_for("user.login", url_after_login=url_for("game.edit",id=id)))

    game = db.session.query(Game).get(id)

    return render_template(
        "game/form.html",
        title="Edit Game",
        action=url_for("game.save"),
        game=game
    )

@game.route("/delete/<int:id>")
def delete(id):
    db.session.query(Game).filter(Game.id == id).delete()
    db.session.commit()
    flash("Game deleted!")
    return redirect(url_for("game.home"))


@game.route("/save", methods=["POST"])
def save():

    id = request.form['id'] or None
    name = request.form['name']
    category = request.form['category']
    device = request.form['device']
    game = Game(id, name, category, device)
    db.session.merge(game)
    db.session.commit()
    return redirect(url_for("game.home"))

def is_logged_in():
    if ("logged_user" not in session or session["logged_user"] == None):
        return False
    return True