#!/usr/bin/python3
from pymongo import MongoClient, ASCENDING
from werkzeug.security import generate_password_hash


client = MongoClient()
db = client.ChambordPi

users = db.Drinks
users.insert_one(
	{
		"name": "Ginger Berry",
		"id": 120,
		"type":"mixed",
		"image":"dirty_martini.png",
		"cost":25,
		"recipe": [
		{
			"type": "Vodka",
			"flavor": None,
			"amount": "3 Tbsp"
		},
		{
			"type": "Ginger Beer",
			"flavor": None,
			"amount": "1/2 cup"
		},
		{
			"type": "Muddled Ginger Slices and Blackberries",
			"flavor": None,
			"amount": "2 and 4"
		},
		{
			"type": "Juice",
			"flavor": "Lime",
			"amount": "1 Tbsp"
		},
		{
			"type": "Ice",
			"flavor": None,
			"amount": "some"
		}
		],
		"available":True,
		"times_ordered":0
		
	})
