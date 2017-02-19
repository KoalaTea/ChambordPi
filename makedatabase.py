#!flask/bin/python
import time
from pymongo import MongoClient, ASCENDING
from werkzeug.security import generate_password_hash
# TODO make usernames unique


client = MongoClient()
client.drop_database("ChambordPi")
db = client.ChambordPi

drinks = db.Drinks
alcohol = db.Alchohol
users = db.Users
orders = db.Orders
mixers = db.Mixers
beer = db.Beer
ingredients = db.Ingredients
statistics = db.Statistics

statistics.insert_one(
    {
        "id": 1,
        "time": int(time.time()*1000) ,
        "total_orders": 0,
        "drink_orders": [
            {"name": "Sky", "Orders": 0},
            {"name": "Malibu", "Orders": 0},
            {"name": "Bacardi", "Orders": 0}
        ]
    }
)

ingredients.insert_one(
        {
            "class": "alcohol",
            "type" : "vodka",
            "name" : "sky",
            "flavor" : None,
            "bottles" : 1,
            "available": True,
            "cost": 25,
            "times_ordered" : 0
        }
)
ingredients.insert_one(
        {
            "class": "alcohol",
            "type" : "",
            "name" : "Jager",
            "flavor" : None,
            "bottles" : 1,
            "available": True,
            "cost": 25,
            "times_ordered" : 0
        }
)
ingredients.insert_one(
        {
            "class": "alcohol",
            "type" : "rum",
            "name" : "Malibu",
            "flavor" : "Coconut",
            "bottles" : 1,
            "available": True,
            "cost": 25,
            "times_ordered" : 0

        }
)
ingredients.insert_one(
        {
            "class": "alcohol",
            "type" : "rum",
            "name" : "Bacardi",
            "flavor" : None,
            "bottles" : 1,
            "available": True,
            "cost": 25,
            "times_ordered" : 0

        }
)
ingredients.insert_one(
        {
            "class": "alcohol",
            "type" : "Gin",
            "name" : "Beefeater",
            "flavor" : None,
            "bottles" : 1,
            "available": True,
            "cost": 25,
            "times_ordered" : 0

        }
)
ingredients.insert_one(
        {
            "class": "alcohol",
            "type" : "Whiskey",
            "name" : "Jack Daniels",
            "flavor" : None,
            "bottles" : 1,
            "available": True,
            "cost": 25,
            "times_ordered" : 0

        }
)
ingredients.insert_one(
        {
            "class": "alcohol",
            "type" : "vodka",
            "name" : "UV Blue",
            "flavor" : None,
            "bottles" : 1,
            "available": True,
            "cost": 25,
            "times_ordered" : 0

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
            "name": "Miller High Life",
            "type": "beer",
            "image": "dirty_martini.png",
            "recipe": [
                {
                    "type": "beer",
                    "flavor": None,
                    "amount": "1 oz"
                }
                            ],
            "available": True,
            "times_ordered" : 0
        }
)
drinks.insert_one(
        {
            "id": 1,
            "name": "Miller Lite",
            "type": "beer",
            "image": "dirty_martini.png",
            "recipe": [
                {
                    "type": "beer",
                    "flavor": None,
                    "amount": "1 oz"
                }
                            ],
            "available": True,
            "times_ordered" : 0
        }
)

drinks.insert_one(
        {
            "id": 2,
            "name": "Budweiser",
            "type": "beer",
            "image": "dirty_martini.png",
            "recipe": [
                {
                    "type": "beer",
                    "flavor": None,
                    "amount": "1 oz"
                }
                            ],
            "available": True,
            "times_ordered" : 0
        }
)

drinks.insert_one(
        {
            "id": 3,
            "name": "Shock Top",
            "type": "beer",
            "image": "dirty_martini.png",
            "recipe": [
                {
                    "type": "beer",
                    "flavor": None,
                    "amount": "1 oz"
                }
                            ],
            "available": True,
            "times_ordered" : 0
        }
)

users.create_index([("username", ASCENDING)], unique=True)

users.insert_one(
        {
            "username" : "koalatea",
            "password" : generate_password_hash("temporary2017koalatea"),
            "credits" : 1000000,
            "roles" : [ "bartender", "admin", "user" ]
        }
)
