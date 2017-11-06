#!/usr/bin/python3
from pymongo import MongoClient, ASCENDING
from werkzeug.security import generate_password_hash
import getpass

username = input("Username: ")
password = getpass.getpass()

client = MongoClient()
db = client.ChambordPi

users = db.Users
users.update_one({"username":username},
	{
		"$set":{
			"password" : generate_password_hash(password)
		}
        }
)
