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
import json
from bson import json_util
from bson.json_util import dumps

app = Flask(__name__)
app.config ['MONGO_URI'] = 'mongodb://localhost:27020/Pokemon_Database'
mongo = PyMongo(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/pokemon')
def getPokemonData():
    data = mongo.db.pokemon.find()
    datalist=[]
    for item in data:
        item.pop("_id")
        ObjectName = [v for v in item.values()]
        datalist.append(ObjectName)
    return jsonify(datalist)

@app.route('/graphcount')
def getGraphCount():
    genrationOne={
        'Bug': 0,
        'Electric':0,
        'Fire':0,
        'Grass':0,
        'Normal':0,
        'Rock':0,
        'Dark':0,
        'Fairy':0,
        'Flying':0,
        'Ground':0,
        'Poison':0,
        'Steel':0,
        'Water':0,
        'Dragon':0,
        'Fighting':0,
        'Ghost':0,
        'Ice':0,
        'Psychic':0,
        'Water':0,
        'Generation':1
    }
    genrationTwo={
        'Bug': 0,
        'Electric':0,
        'Fire':0,
        'Grass':0,
        'Normal':0,
        'Rock':0,
        'Dark':0,
        'Fairy':0,
        'Flying':0,
        'Ground':0,
        'Poison':0,
        'Steel':0,
        'Water':0,
        'Dragon':0,
        'Fighting':0,
        'Ghost':0,
        'Ice':0,
        'Psychic':0,
        'Water':0,
        'Generation':2
    }
    data = mongo.db.pokemon.find()
    for types in data:
        if types['Type 1'] in genrationOne:# and types['Generation']=='1':
            firstType= types['Type 1']
            secondType= types['Type 2']
            try:
                genrationOne[firstType]= genrationOne[firstType]+1 
                genrationOne[secondType]=genrationOne[secondType]+1
            except:
                next

        

        #if types['Type 2'] in genrationOne and types['Generation']=='1':
            #secondType= types['Type 2']
            #genrationOne[secondType]= genrationOne[secondType]+1
        
    return genrationOne 
        
        
    

    

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)



