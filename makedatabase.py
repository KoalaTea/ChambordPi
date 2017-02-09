#!flask/bin/python
from pymongo import MongoClient
from werkzeug.security import generate_password_hash
# TODO make usernames unique


client = MongoClient()
client.drop_database("ChambordPi")
db = client.ChambordPi

drinks = db.Drinks
alchohol = db.Alchohol
users = db.Users
orders = db.Orders
mixers = db.Mixers
beer = db.Beer

alchohol.insert_one(
        {
            "type" : "vodka",
            "name" : "sky",
            "flavor" : None,
            "bottles" : 1
        }
)
alchohol.insert_one(
        {
            "type" : "liqueur",
            "name" : "chambord",
            "flavor" : "raspberry",
            "bottles" : 1
        }
)
alchohol.insert_one(
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
            "password" : generate_password_hash("test"),
            "credits" : 1000000,
            "roles" : [ "bartender", "admin", "user" ]
        }
)

users.insert_one(
        {
            "username" : "john",
            "password" : generate_password_hash("test"),
            "credits" : 100,
            "roles" : [ "user" ]
        }
)

users.insert_one(
        {
            "username" : "admin",
            "password" : generate_password_hash("admin"),
            "credits" : 100,
            "roles" : [ "user", "admin" ]
        }
)


orders.insert_one(
        {
            "drink" : {
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
                ]
            },
            "user" : "koalatea"
        }
)
