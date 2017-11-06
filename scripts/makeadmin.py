#!/usr/bin/python3
from pymongo import MongoClient, ASCENDING
from werkzeug.security import generate_password_hash
import getpass

username = input("Username: ")

client = MongoClient()
db = client.ChambordPi

users = db.Users
users.update_one({"username" : username},
	{
	    '$set':{ 
            "credits" : 1000000000,
            "roles" : [ "user", "admin", "bartender" ]
            }
	}
)
