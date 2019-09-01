from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/pokedatabase"

mongo = PyMongo(app)

@app.route("/")
def index():
    pokemon = mongo.db.pokedatabase.find_one()
    return render_template("index.html", pokemon=pokemon)

@app.route('/pokemon')
def getPokemonData():
    data = mongo.db.pokemon.find()
    datalist = []
    for item in data:
        item.pop("__id")
        ObjectName = [v for v in item.values()]
        datalist.append(ObjectName)
    return jsonify(datalist)

if __name__ == "__main__":
    app.run(debug=True)