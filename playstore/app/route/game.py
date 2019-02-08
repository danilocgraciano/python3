from flask import Blueprint, render_template, request, redirect, session, flash, url_for

from app import db
from app.model import Game, Category

game = Blueprint("game",__name__)

@game.route("/")
def home():
    games = db.session.query(Game).order_by(Game.name)

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
    categories = db.session.query(Category).order_by(Category.name)

    return render_template(
        "game/form.html",
        title="New Game",
        action=url_for("game.save"),
        game=game,
        categories=categories
    )

@game.route("/edit/<int:id>")
def edit(id):
    if (not is_logged_in()):
        return redirect(url_for("user.login", url_after_login=url_for("game.edit",id=id)))

    game = db.session.query(Game).get(id)
    categories = db.session.query(Category).order_by(Category.name)

    return render_template(
        "game/form.html",
        title="Edit Game",
        action=url_for("game.save"),
        game=game,
        categories=categories
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
    game = Game(None, None, None, None)
    if (id):
        game = db.session.query(Game).get(id)

    game.name = request.form['name']
    category_id = request.form['category.id']
    game.category = db.session.query(Category).get(category_id)
    #BOTH WORKS
    #game.category = db.session.query(Category).get(category_id)
    #game.category_id = category_id
    game.device = request.form['device']


    db.session.merge(game)
    db.session.commit()
    return redirect(url_for("game.home"))

def is_logged_in():
    if ("logged_user" not in session or session["logged_user"] == None):
        return False
    return True