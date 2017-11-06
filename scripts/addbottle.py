#!/usr/bin/python3
from pymongo import MongoClient, ASCENDING
from werkzeug.security import generate_password_hash
import getpass

myclass = input("class: ")
alch = input("Alco: ")
flavor = input("Flavor: ")
if flavor == "none":
	flavor = None
type= input("type: ")

client = MongoClient()
db = client.ChambordPi

ing = db.Ingredients
theing = ing.find_one({'name': alch, 'flavor': flavor})
if theing is not None:
	ing.update_one({'name': alch, 'flavor':flavor},
		{
		    '$inc':{ 
			'bottles': 1
		    }
		}
	)
else:
	if myclass == "mixer":
		ing.insert_one({"name": alch, "available": True, 'class': myclass, 'bottles':1})
	else:
		ing.insert_one({"name": alch, "available": True, 'cost':25, "bottles":1, "flavor":flavor, "type":type, "class": myclass, "times_ordered":0})
