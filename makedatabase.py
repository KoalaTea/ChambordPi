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
ingredients = db.Ingredients

ingredients.insert_one(
        {
            "class": "alchohol",
            "type" : "vodka",
            "name" : "sky",
            "flavor" : None,
            "bottles" : 1,
            "available": True,
            "cost": 25
        }
)
ingredients.insert_one(
        {
            "class": "alchohol",
            "type" : "",
            "name" : "Jager",
            "flavor" : None,
            "bottles" : 1,
            "available": True,
            "cost": 25
        }
)
ingredients.insert_one(
        {
            "class": "alchohol",
            "type" : "rum",
            "name" : "Malibu",
            "flavor" : "Coconut",
            "bottles" : 1,
            "available": True,
            "cost": 25

        }
)
ingredients.insert_one(
        {
            "class": "alchohol",
            "type" : "rum",
            "name" : "Bacardi",
            "flavor" : None,
            "bottles" : 1,
            "available": True,
            "cost": 25

        }
)
ingredients.insert_one(
        {
            "class": "alchohol",
            "type" : "Gin",
            "name" : "Beefeater",
            "flavor" : None,
            "bottles" : 1,
            "available": True,
            "cost": 25

        }
)
ingredients.insert_one(
        {
            "class": "alchohol",
            "type" : "Whiskey",
            "name" : "Jack Daniels",
            "flavor" : None,
            "bottles" : 1,
            "available": True,
            "cost": 25

        }
)
ingredients.insert_one(
        {
            "class": "alchohol",
            "type" : "vodka",
            "name" : "UV Blue",
            "flavor" : None,
            "bottles" : 1,
            "available": True,
            "cost": 25

        }
)


ingredients.insert_one(
        {
            "class": "mixer",
            "name": "Orange Juice",
            "bottles": 5,
            "available": True
        }
)
ingredients.insert_one(
        {
            "class": "mixer",
            "name": "Sprite",
            "bottles": 5,
            "available": True
        }
)
ingredients.insert_one(
        {
            "class": "mixer",
            "name": "Coca-Cola",
            "bottles": 5,
            "available": True
        }
)
ingredients.insert_one(
        {
            "class": "mixer",
            "name": "Ginger Ale",
            "bottles": 5,
            "available": True
        }
)
ingredients.insert_one(
        {
            "class": "mixer",
            "name": "Lemonade",
            "bottles": 5,
            "available": True
        }
)
ingredients.insert_one(
        {
            "class": "mixer",
            "name": "Tonic",
            "bottles": 5,
            "available": True
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
