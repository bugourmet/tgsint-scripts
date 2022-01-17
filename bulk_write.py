import pymongo
from pymongo import InsertOne
import json

client = pymongo.MongoClient("DBCONNECTIONURL")
db = client.get_database("database")
collection = db.get_collection("persons")
requesting = []

with open("formatted.txt", 'r') as f: ##loads the formatted file (json) and populates the DB
     contents = json.loads(f.read())
     for jsonbj in contents:
         requesting.append(InsertOne(jsonbj))

result = collection.bulk_write(requesting)
client.close()