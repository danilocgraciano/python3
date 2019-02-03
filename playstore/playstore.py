from flask import Flask, render_template
from game import Game

app = Flask(__name__)

@app.route("/")
def home():

    pou = Game("pou","Kids","Moto G2")
    subway_surfers = Game("subway surfers", "Kids", "Moto G3")
    my_talking_tom = Game("Mm talking tom", "Kids", "Moto G3")
    despicable_me = Game("despicable me","Kids","iPhone")
    zombie_tsunami = Game("zombie tsunami","Kids","iPhone")

    games = []
    games.append(pou)
    games.append(subway_surfers)
    games.append(my_talking_tom)
    games.append(despicable_me)
    games.append(zombie_tsunami)

    return render_template(
        "list.html",
        title="My Playstore",
        list=games
    )

#app.run(host='0.0.0.0', port=8080)
app.run()