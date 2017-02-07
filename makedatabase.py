#!flask/bin/python
from pymongo import MongoClient

client = MongoClient()
client.drop_database("ChambordPi")
db = client.ChambordPi

drinks = db.Drinks
alchohal = db.Alchohal
users = db.Users
orders = db.Orders
mixers = db.Mixers
beer = db.Beer

alchohal.insert_one(
        {
            "type" : "vodka",
            "name" : "sky",
            "flavor" : None,
            "bottles" : 1
        }
 )
alchohal.insert_one(
        {
            "type" : "liqueur",
            "name" : "chambord",
            "flavor" : "raspberry",
            "bottles" : 1
        }
)
alchohal.insert_one(
        {
            "type" : "vodka",
            "name" : "grey goose",
            "flavor" : None,
            "bottles" : 0
        }
)

drinks.insert_one(
        {
            "name" : "Has the stuff test",
            "type" : "mixed",
            "recipe" : [
                {
                    "type" : "vodka",
                    "flavor" : None,
                    "ammount" : "1 oz"
                },
                {
                    "type" : "liqueur",
                    "flavor" : "raspberry",
                    "ammount" : "1 oz"
                },
                {
                    "type" : "mixer",
                    "name" : "sprite",
                    "ammount" : "fill"
                }
            ],
            "available" : True
        }
)

drinks.insert_one(
        {
            "name" : "Don't have",
            "type" : "shot",
            "recipe" : [
                {
                    "type" : "vodka",
                    "flavor" : None,
                    "ammount" : "half"
                },
                {
                    "type" : "gin",
                    "flavor" : None,
                    "ammount" : "half"
                }
            ],
            "available" : False
        }
)

users.insert_one(
        {
            "username" : "koalatea",
            "password" : "test",
            "credits" : 1000000,
            "roles" : [ "bartender", "admin", "users" ]
        }
)

orders.insert_one(
        {
            "name" : "Has the stuff test",
            "user" : "koalatea"
        }
)


