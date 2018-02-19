#! /usr/bin/python
import time
from pymongo import MongoClient, ASCENDING
from werkzeug.security import generate_password_hash
# TODO make usernames unique

def make_database(db_name):
    client = MongoClient()
    client.drop_database(db_name)
    db = client[db_name]

    drinks = db.drink
    alcohol = db.alchohol
    users = db.user
    orders = db.order
    mixers = db.mixer
    beer = db.beer
    ingredients = db.ingredient

    ingredients.insert_one(
            {
                "ingredient_class": "alcohol",
                "ingredient_type" : "vodka",
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
                "ingredient_class": "alcohol",
                "ingredient_type" : "",
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
                "ingredient_class": "alcohol",
                "ingredient_type" : "rum",
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
                "ingredient_class": "alcohol",
                "ingredient_type" : "rum",
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
                "ingredient_class": "alcohol",
                "ingredient_type" : "Gin",
                "name" : "New Amsterdam",
                "flavor" : None,
                "bottles" : 1,
                "available": True,
                "cost": 25,
                "times_ordered" : 0

            }
    )
    ingredients.insert_one(
            {
                "ingredient_class": "alcohol",
                "ingredient_type" : "Whiskey",
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
                "ingredient_class": "alcohol",
                "ingredient_type" : "vodka",
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
                "ingredient_class": "mixer",
                "name": "Orange Juice",
                "bottles": 5,
                "available": True
            }
    )
    ingredients.insert_one(
            {
                "ingredient_class": "mixer",
                "name": "Sprite",
                "bottles": 5,
                "available": True
            }
    )
    ingredients.insert_one(
            {
                "ingredient_class": "mixer",
                "name": "Coca-Cola",
                "bottles": 5,
                "available": True
            }
    )
    ingredients.insert_one(
            {
                "ingredient_class": "mixer",
                "name": "Ginger Ale",
                "bottles": 5,
                "available": True
            }
    )
    ingredients.insert_one(
            {
                "ingredient_class": "mixer",
                "name": "Lemonade",
                "bottles": 5,
                "available": True
            }
    )
    ingredients.insert_one(
            {
                "ingredient_class": "mixer",
                "name": "Tonic",
                "bottles": 5,
                "available": True
            }
    )

    drinks.insert_one(
            {
                "id": 0,
                "name": "Miller High Life",
                "drink_type": "beer",
                "image": "beer.png",
                "recipe": [
                    {
                        "type": "beer",
                        "flavor": None,
                        "amount": "1 oz"
                    }
                                ],
                "available": True,
                "times_ordered" : 0,
                "cost" : 25
            }
    )

    drinks.insert_one(
            {
                "id": 1,
                "name": "Moscow Mule",
                "drink_type": "mixed",
                "image": "dirty_martini.png",
                "recipe": [
                    {
                        "type": "lime",
                        "flavor": None,
                        "amount": "1/2"
                    },
                    {
                        "type": "vodka",
                        "flavor": None,
                        "amount": "1 part"
                    },
                    {
                        "type": "ginger beer",
                        "flavor": None,
                        "amount": "1 part"
                    }
                                ],
                "available": True,
                "times_ordered" : 0,
                "cost" : 25
           }
    )

    drinks.insert_one(
            {
                "id": 2,
                "name": "Rum and Coke",
                "drink_type": "mixed",
                "image": "dirty_martini.png",
                "recipe": [
                    {
                        "type": "Rum",
                        "flavor": None,
                        "amount": "2 shots"
                    },
                    {
                        "type": "Coca-Cola",
                        "flavor": None,
                        "amount": "2 shots"
                    }
                                ],
                "available": True,
                "times_ordered" : 0,
                "cost" : 50
           }
    )

    drinks.insert_one(
            {
                "id": 3,
                "name": "Whiskey and Coke",
                "drink_type": "mixed",
                "image": "dirty_martini.png",
                "recipe": [
                    {
                        "type": "Whiskey",
                        "flavor": None,
                        "amount": "2 shots"
                    },
                    {
                        "type": "Coca-Cola",
                        "flavor": None,
                        "amount": "2 shots"
                    }
                                ],
                "available": True,
                "times_ordered" : 0,
                "cost" : 50
           }
    )

    drinks.insert_one(
            {
                "id": 4,
                "name": "Whiskey Sour",
                "drink_type": "mixed",
                "image": "dirty_martini.png",
                "recipe": [
                    {
                        "type": "Whiskey",
                        "flavor": None,
                        "amount": "2 shots"
                    },
                    {
                        "type": "Lemon Juice",
                        "flavor": None,
                        "amount": "2 shots"
                    }
                                ],
                "available": True,
                "times_ordered" : 0,
                "cost" : 50
           }
    )

    drinks.insert_one(
            {
                "id": 5,
                "name": "Rum and Sprite",
                "drink_type": "mixed",
                "image": "dirty_martini.png",
                "recipe": [
                    {
                        "type": "Rum",
                        "flavor": None,
                        "amount": "2 shots"
                    },
                    {
                        "type": "Sprite",
                        "flavor": None,
                        "amount": "2 shots"
                    }
                                ],
                "available": True,
                "times_ordered" : 0,
                "cost" : 50
           }
    )

    drinks.insert_one(
            {
                "id": 6,
                "name": "Shirley Temple",
                "drink_type": "mixed",
                "image": "dirty_martini.png",
                "recipe": [
                    {
                        "type": "Grenadine",
                        "flavor": None,
                        "amount": "1 shot"
                    },
                    {
                        "type": "Ginger ale",
                        "flavor": None,
                        "amount": "1 shot"
                    },
                    {
                        "type": "Sprite",
                        "flavor": None,
                        "amount": "1 shot"
                    },
                    {
                        "type": "Sky",
                        "flavor": None,
                        "amount": "1 shot"
                    }
                                ],
                "available": True,
                "times_ordered" : 0,
                "cost" : 25
           }
    )

    users.create_index([("username", ASCENDING)], unique=True)

    users.insert_one(
            {
                "username" : "koalatea",
                "password" : generate_password_hash("temporary2017koalatea"),
                "credits" : 1000000,
                "roles" : [ "bartender", "admin", "user" ],
                "drinks_ordered" : 0
            }
    )
    users.insert_one(
            {
                "username" : "user",
                "password" : generate_password_hash("temporary2017koalatea"),
                "credits" : 1000000,
                "roles" : [ "user" ],
                "drinks_ordered" : 0
            }
    )
    users.insert_one(
            {
                "username" : "bartender",
                "password" : generate_password_hash("bartender"),
                "credits" : 1000000,
                "roles" : [ "bartender" ],
                "drinks_ordered" : 0
            }
    )

if __name__ == '__main__':
    make_database('testfromcmd')
