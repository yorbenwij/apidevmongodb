from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:itf@cluster0.kxuy1ns.mongodb.net/?retryWrites=true&w=majority")

db = client.country_db

collection_name = db["country_collection"]
