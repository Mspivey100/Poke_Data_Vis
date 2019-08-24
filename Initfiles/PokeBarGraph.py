import pymongo
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

data=db.pokedatabase.find()

