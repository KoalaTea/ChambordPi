#!/usr/bin/python3
from pymongo import MongoClient, ASCENDING
from werkzeug.security import generate_password_hash


client = MongoClient()
db = client.ChambordPi

users = db.Drinks
users.delete_one({"name": "PBR"})
