#!/usr/bin/python3
from pymongo import MongoClient, ASCENDING
from werkzeug.security import generate_password_hash
import getpass

username = input("Username: ")

client = MongoClient()
db = client.ChambordPi

users = db.Users
users.delete_one({"username" : username})
