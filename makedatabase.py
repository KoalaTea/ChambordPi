#!flask/bin/python
from pymongo import MongoClient, ASCENDING
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

drinks.create_index([("id", ASCENDING)], unique=True)

drinks.insert_one(
        {
            "id": 0,
            "name": "Mystery Drink",
            "type": "mixed",
            "image": "dirty_martini.png",
            "recipe": [
                {
                    "type": "vodka",
                    "flavor": None,
                    "amount": "1 oz"
                },
                {
                    "type": "liqueur",
                    "flavor": "raspberry",
                    "amount": "1 oz"
                },
                {
                    "type": "mixer",
                    "name": "sprite",
                    "amount": "fill"
                }
            ],
            "available": True
        }
)
drinks.insert_one(
        {
            "id": 1,
            "name": "Mystery Drink",
            "type": "mixed",
            "image": "dirty_martini.png",
            "recipe": [
                {
                    "type": "vodka",
                    "flavor": None,
                    "amount": "1 oz"
                },
                {
                    "type": "liqueur",
                    "flavor": "raspberry",
                    "amount": "1 oz"
                },
                {
                    "type": "mixer",
                    "name": "sprite",
                    "amount": "fill"
                }
            ],
            "available": True
        }
)
drinks.insert_one(
        {
            "id": 2,
            "name": "Mystery Drink",
            "type": "mixed",
            "image": "dirty_martini.png",
            "recipe": [
                {
                    "type": "vodka",
                    "flavor": None,
                    "amount": "1 oz"
                },
                {
                    "type": "liqueur",
                    "flavor": "raspberry",
                    "amount": "1 oz"
                },
                {
                    "type": "mixer",
                    "name": "sprite",
                    "amount": "fill"
                }
            ],
            "available": True
        }
)
drinks.insert_one(
        {
            "id": 3,
            "name": "Not Free",
            "type": "mixed",
            "cost": 50,
            "image": "dirty_martini.png",
            "recipe": [
                {
                    "type": "vodka",
                    "flavor": None,
                    "amount": "1 oz"
                },
                {
                    "type": "liqueur",
                    "flavor": "raspberry",
                    "amount": "1 oz"
                },
                {
                    "type": "mixer",
                    "name": "sprite",
                    "amount": "fill"
                }
            ],
            "available": True
        }
)
drinks.insert_one(
        {
            "id": 4,
            "name": "Expensive",
            "type": "mixed",
            "cost": 10000000,
            "image": "dirty_martini.png",
            "recipe": [
                {
                    "type": "vodka",
                    "flavor": None,
                    "amount": "1 oz"
                },
                {
                    "type": "liqueur",
                    "flavor": "raspberry",
                    "amount": "1 oz"
                },
                {
                    "type": "mixer",
                    "name": "sprite",
                    "amount": "fill"
                }
            ],
            "available": True
        }
)
drinks.insert_one(
        {
            "id": "5",
            "name" : "Godfather",
            "type" : "mixed",
            "recipe" : [
                {
                    "type" : "amerreto",
                    "flavor" : None,
                    "ammount" : "half"
                },
                {
                    "type" : "scotch",
                    "flavor" : None,
                    "ammount" : "half"
                }
            ],
            "available" : False
        }
)

users.create_index([("username", ASCENDING)], unique=True)

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
users.insert_one(
        {
            "username" : "usrtest",
            "password" : generate_password_hash("test"),
            "credits" : 100,
            "roles" : [ "user"]
        }
)


orders.insert_one(
        {
            "name" : "DrinkOne",
            "type" : "mixed",
            "image": "dirty_martini.png",
            "timeOrdered": "152321",
            "user": "koalatea",
            "status": "Queued"
        }
)

orders.insert_one(
        {
            "name" : "DrinkTwo",
            "type" : "mixed",
            "image": "dirty_martini.png",
            "timeOrdered": "152321",
            "user": "koalatea",
            "status": "Inprogress"
        }
)
orders.insert_one(
        {
            "name" : "DrinkThree",
            "type" : "mixed",
            "image": "dirty_martini.png",
            "timeOrdered": "152321",
            "user": "koalatea",
            "status": "Ready"
        }
)

