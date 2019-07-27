from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import  Api

app = Flask(__name__)

app.config['MONGO_URI'] = ''
app.database = PyMongo(app)
app.cars_collection = app.database.db.cars


# Create api
api = Api(app)



