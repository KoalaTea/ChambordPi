#!/usr/bin/python3
from pymongo import MongoClient, ASCENDING
from werkzeug.security import generate_password_hash
import getpass

username = input("Username: ")

client = MongoClient()
db = client.ChambordPi

users = db.PastOrders
past = users.find()
for i in past:
    users.delete_one({"_id" : i['_id']})
