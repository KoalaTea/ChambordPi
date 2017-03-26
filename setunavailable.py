#!/usr/bin/python3
from pymongo import MongoClient, ASCENDING
from werkzeug.security import generate_password_hash
import getpass

username = input("Drink: ")

client = MongoClient()
db = client.ChambordPi

users = db.Drinks
users.update_one({"name" : username},
	{
	    '$set':{ 
            "available" : False
            }
	}
)
