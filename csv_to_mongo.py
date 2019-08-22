import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
#CSV to JSON Conversion
csvfile = open('Pokemon.csv', 'r')
reader = csv.DictReader( csvfile )
mongo_client=MongoClient('localhost', 27020) 
header= ["PokeIndex","Name","Type 1","Type 2","Total","HP","Attack","Defense","SpAtk","SpDef","Speed","Generation","Legendary"]
db=mongo_client.Pokemon_Database
coll = db.pokedatabase
coll.create_index('Name',unique=True)
for each in reader:
    row={}
    for field in header:
        row[field]=each[field]
    coll.insert_one(row)