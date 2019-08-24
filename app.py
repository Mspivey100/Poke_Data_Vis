from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import os


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def home():
    poke_data = mongo.db.Pokemon_Database.find_one()

    return render_template("index.html", pokemon_data = poke_data)

