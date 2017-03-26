#!/usr/bin/python3
from pymongo import MongoClient, ASCENDING
from werkzeug.security import generate_password_hash


client = MongoClient()
db = client.ChambordPi

users = db.Drinks
users.insert_one(
	{
		"name": "Hot Pepper",
		"id": 111,
		"type":"mixed",
		"image":"dirty_martini.png",
		"cost":25,
		"recipe": [
		{
			"type": "Dr Pepper mini",
			"flavor": None,
			"amount": "drink some"
		},
		{
			"type": "fireball",
			"flavor": None,
			"amount": "fill"
		}
		],
		"available":True,
		"times_ordered":0
		
	})
