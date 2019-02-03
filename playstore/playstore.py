from flask import Flask, render_template, request, redirect
from game import Game

games = []
pou = Game("pou","Kids","Moto G2")
subway_surfers = Game("subway surfers", "Kids", "Moto G3")
my_talking_tom = Game("Mm talking tom", "Kids", "Moto G3")
despicable_me = Game("despicable me","Kids","iPhone")
zombie_tsunami = Game("zombie tsunami","Kids","iPhone")

games.append(pou)
games.append(subway_surfers)
games.append(my_talking_tom)
games.append(despicable_me)
games.append(zombie_tsunami)


app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "list.html",
        title="Games",
        list=games
    )

@app.route("/new")
def new():
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
    return redirect("/")

#app.run(host='0.0.0.0', port=8080)
app.run(debug=True)