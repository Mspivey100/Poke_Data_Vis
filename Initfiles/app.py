from flask_pymongo import PyMongo
import flask 
import os 
import sys
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect
)

app = Flask(__name__)
app.config ['MONGO_URI'] = 'mongodb://localhost:27020/Pokemon_Database'
mongo = PyMongo(app)

@app.route('/')
def home():
    data = mongo.db.pokemon.find()
    datalist=[]
    for item in data:
        item.pop("_id")
        ObjectName = [v for v in item.values()]
        datalist.append(ObjectName)
    return jsonify(datalist)

