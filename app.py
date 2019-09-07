from flask_pymongo import PyMongo
import flask 
import os 
import sys
import math
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
app.config ['MONGO_URI'] = 'mongodb://localhost:27017/Pokemon_Database'
mongo = PyMongo(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/pokemon')
def getPokemonData():
    data = mongo.db.pokedatabase.find()
    datalist=[]
    for item in data:
        item.pop("_id")
        datalist.append(item)
    return jsonify(datalist)

@app.route('/graphcount')
def getGraphCount():
    #dict of counters
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
        'Generation':1
    }
    
    data = mongo.db.pokemon.find()
    for types in data:
        # if you find the type in the gen dict
        if types['Type 1'] in genrationOne:# and types['Generation']=='1':
            #set type 1 to a variable and type 2 to a variable
            firstType= types['Type 1']
            secondType= types['Type 2']
            try:
                genrationOne[firstType]= genrationOne[firstType]+1 
                genrationOne[secondType]=genrationOne[secondType]+1
            except:
                next 
        
    return genrationOne 
        
        
@app.route('/avgtotalstats') 
def getTotalStats():
   #getting the total stats
    statsByGen={
        '1':0,
        '2':0,
        '3':0,
        '4':0,
        '5':0,
        '6':0
    }
    #counts for each pokemon by generation
    statsByGenCounter={
        '1':0,
        '2':0,
        '3':0,
        '4':0,
        '5':0,
        '6':0
    }

    data = mongo.db.pokemon.find()
    for stats in data:
        if stats['Generation'] in statsByGen:
            pokeGen=stats['Generation']
            pokeStats=stats['Total']
            statsByGenCounter[pokeGen] = statsByGenCounter[pokeGen] + 1
            print(f'{statsByGenCounter}')
            statsByGen[pokeGen] += int(pokeStats)
    avgStatsByGen = {k :math.ceil( statsByGen[k] / statsByGenCounter[k] ) for k in statsByGen}
    return avgStatsByGen

@app.route('/pokedex',methods =['GET','POST'])
def PokeDex():
    if request.method == 'POST':
        PokemonName=request.form.get('Name')
        data = mongo.db.pokemon.find_one({'Name': Name })
        print (data)
    return 'data'


    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)



