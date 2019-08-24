from flask_pymongo import PyMongo
import flask 
import os 
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect
)

conn = 'mongodb://localhost:27020'
client = pymongo.MongoClient(conn)

db=client.Pokemon_Database

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27020/Pokemon_Database"
mongo = PyMongo(app)

@app.route("/")
def home_page():
    data = mongo.db.pokemon.find()
    return render_template("index.html",
        data=data)