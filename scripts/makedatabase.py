#! /usr/bin/python
import time
from pymongo import MongoClient, ASCENDING
from werkzeug.security import generate_password_hash
# TODO make usernames unique


client = MongoClient()
client.drop_database("ChambordPi")
db = client.ChambordPi

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
            "measure" : "bottles",
            "stock": 1,
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
            "measure" : "bottles",
            "stock": 1,
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
            "measure" : "bottles",
            "stock": 1,
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
            "measure" : "bottles",
            "stock": 1,
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
            "measure" : "bottles",
            "stock": 1,
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
            "measure" : "bottles",
            "stock": 1,
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
            "measure" : "bottles",
            "stock": 1,
            "available": True,
            "cost": 25,
            "times_ordered" : 0

        }
)


ingredients.insert_one(
        {
            "ingredient_class": "mixer",
            "name": "Orange Juice",
            "measure" : "bottles",
            "stock": 1,
            "available": True
        }
)
ingredients.insert_one(
        {
            "ingredient_class": "mixer",
            "name": "Sprite",
            "measure" : "bottles",
            "stock": 1,
            "available": True
        }
)
ingredients.insert_one(
        {
            "ingredient_class": "mixer",
            "name": "Coca-Cola",
            "measure" : "bottles",
            "stock": 1,
            "available": True
        }
)
ingredients.insert_one(
        {
            "ingredient_class": "mixer",
            "name": "Ginger Ale",
            "measure" : "bottles",
            "stock": 1,
            "available": True
        }
)
ingredients.insert_one(
        {
            "ingredient_class": "mixer",
            "name": "Lemonade",
            "measure" : "bottles",
            "stock": 1,
            "available": True
        }
)
ingredients.insert_one(
        {
            "ingredient_class": "mixer",
            "name": "Tonic",
            "measure" : "bottles",
            "stock": 1,
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
            "name": "Miller Lite",
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
            "cost" : 10
       }
)

drinks.insert_one(
        {
            "id": 2,
            "name": "Budweiser",
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
            "cost" : 10
       }
)

drinks.insert_one(
        {
            "id": 3,
            "name": "Shock Top",
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
            "id": 4,
            "name": "Screwdriver",
            "drink_type": "mixed",
            "image": "dirty_martini.png",
            "recipe": [
                {
                    "type": "vodka",
                    "flavor": None,
                    "amount": "1 oz"
                },
                {
                    "type": "orange juice",
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
            "id": 5,
            "name": "Godfather",
            "drink_type": "mixed",
            "image": "dirty_martini.png",
            "recipe": [
                {
                    "type": "amaretto",
                    "flavor": None,
                    "amount": "1 oz"
                },
                {
                    "type": "whiskey",
                    "flavor": None,
                    "amount": "1 oz"
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
            "name": "Mojito",
            "drink_type": "mixed",
            "image": "dirty_martini.png",
            "recipe": [
                {
                    "type": "lime",
                    "flavor": None,
                    "amount": "1/2"
                },
                {
                    "type": "white rum",
                    "flavor": None,
                    "amount": "2 oz"
                },
                {
                    "type": "club soda",
                    "flavor": None,
                    "amount": "2 oz"
                },
                {
                    "type": "mint",
                    "flavor": None,
                    "amount": "muddled"
                },
                {
                    "type": "sugar",
                    "flavor": None,
                    "amount": "tablespoon of sugar"
                }
                            ],
            "available": True,
            "times_ordered" : 0,
            "cost" : 50
       }
)

drinks.insert_one(
        {
            "id": 7,
            "name": "Dark and Stormy",
            "drink_type": "mixed",
            "image": "dirty_martini.png",
            "recipe": [
                {
                    "type": "lime",
                    "flavor": None,
                    "amount": "1/2"
                },
                {
                    "type": "rum",
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
            "id": 8,
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
            "id": 9,
            "name": "Rum Chata TODO",
            "drink_type": "mixed",
            "image": "dirty_martini.png",
            "recipe": [
                {
                    "type": "fireball",
                    "flavor": None,
                    "amount": "1 part"
                },
                {
                    "type": "rum chata",
                    "flavor": None,
                    "amount": "3 parts"
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
            "id": 10,
            "name": "Electric Boogaloo",
            "drink_type": "mixed",
            "image": "dirty_martini.png",
            "recipe": [
                {
                    "type": "UV Blue",
                    "flavor": None,
                    "amount": "3 shots"
                },
                {
                    "type": "Lemon juice",
                    "flavor": None,
                    "amount": "2 shots"
                },
                {
                    "type": "Sprite",
                    "flavor": None,
                    "amount": "Fill rest"
                }
                            ],
            "available": True,
            "times_ordered" : 0,
            "cost" : 75
       }
)

drinks.insert_one(
        {
            "id": 11,
            "name": "Martini",
            "drink_type": "mixed",
            "image": "dirty_martini.png",
            "recipe": [
                {
                    "type": "Gin",
                    "flavor": None,
                    "amount": "3 shots"
                },
                {
                    "type": "Dry vermouth",
                    "flavor": None,
                    "amount": "2 shots"
                },
                {
                    "type": "Crushed ice",
                    "flavor": None,
                    "amount": "Varies"
                }
                            ],
            "available": True,
            "times_ordered" : 0,
            "cost" : 75
       }
)

drinks.insert_one(
        {
            "id": 12,
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
            "id": 13,
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
            "id": 14,
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
            "id": 15,
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
            "id": 16,
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

drinks.insert_one(
        {
            "id": 17,
            "name": "Yellow Thunder",
            "drink_type": "mixed",
            "image": "dirty_martini.png",
            "recipe": [
                {
                    "type": "Vodka",
                    "flavor": None,
                    "amount": "2 shots"
                },
                {
                    "type": "Lemonade",
                    "flavor": None,
                    "amount": "1 shot"
                }
                            ],
            "available": True,
            "times_ordered" : 0,
            "cost" : 50
       }
)

drinks.insert_one(
        {
            "id": 18,
            "name": "Jagerbomb",
            "drink_type": "mixed",
            "image": "dirty_martini.png",
            "recipe": [
                {
                    "type": "Jager",
                    "flavor": None,
                    "amount": "1 shot"
                },
                {
                    "type": "Red Bull",
                    "flavor": None,
                    "amount": "1 shot"
                }
                            ],
            "available": True,
            "times_ordered" : 0,
            "cost" : 25
       }
)

drinks.insert_one(
        {
            "id": 19,
            "name": "Gin Sour",
            "drink_type": "mixed",
            "image": "dirty_martini.png",
            "recipe": [
                {
                    "type": "Gin",
                    "flavor": None,
                    "amount": "2 shots"
                },
                {
                    "type": "Lemon juice",
                    "flavor": None,
                    "amount": "1 shot"
                },
                {
                    "type": "Sugar",
                    "flavor": None,
                    "amount": "Tablespoon"
                }
                            ],
            "available": True,
            "times_ordered" : 0,
            "cost" : 25
       }
)

drinks.insert_one(
        {
            "id": 20,
            "name": "Blowjob Shot",
            "drink_type": "shot",
            "image": "dirty_martini.png",
            "recipe": [
                {
                    "type": "Khalua",
                    "flavor": None,
                    "amount": "1/2 shot"
                },
                {
                    "type": "Irish cream",
                    "flavor": None,
                    "amount": "1/2 shot"
                }
                            ],
            "available": True,
            "times_ordered" : 0,
            "cost" : 25
       }
)

drinks.insert_one(
        {
            "id": 21,
            "name": "Gin and Tonic",
            "drink_type": "mixed",
            "image": "dirty_martini.png",
            "recipe": [
                {
                    "type": "Gin",
                    "flavor": None,
                    "amount": "2 shots"
                },
                {
                    "type": "Tonic",
                    "flavor": None,
                    "amount": "1 shot"
                }
                            ],
            "available": True,
            "times_ordered" : 0,
            "cost" : 50
       }
)

drinks.insert_one(
        {
            "id": 22,
            "name": "Alexander",
            "drink_type": "mixed",
            "image": "dirty_martini.png",
            "recipe": [
                {
                    "type": "Brandy",
                    "flavor": None,
                    "amount": "1 shot"
                },
                {
                    "type": "Cream",
                    "flavor": None,
                    "amount": "1 shot"
                },
                {
                    "type": "Creme de cacao",
                    "flavor": None,
                    "amount": "1 shot"
                }
                            ],
            "available": True,
            "times_ordered" : 0,
            "cost" : 50
       }
)

drinks.insert_one(
        {
            "id": 23,
            "name": "White Russian",
            "drink_type": "mixed",
            "image": "dirty_martini.png",
            "recipe": [
                {
                    "type": "Coffee liqueur",
                    "flavor": None,
                    "amount": "1 shot"
                },
                {
                    "type": "Vodka",
                    "flavor": None,
                    "amount": "2 shots TODO"
                },
                {
                    "type": "Cream",
                    "flavor": None,
                    "amount": "2 shots"
                }
                            ],
            "available": True,
            "times_ordered" : 0,
            "cost" : 75
       }
)

drinks.insert_one(
        {
            "id": 24,
            "name": "Vodka Red Bull",
            "drink_type": "mixed",
            "image": "dirty_martini.png",
            "recipe": [
                {
                    "type": "Vodka",
                    "flavor": None,
                    "amount": "2 shots"
                },
                {
                    "type": "Red Bull",
                    "flavor": None,
                    "amount": "1 cup"
                }
                            ],
            "available": True,
            "times_ordered" : 0,
            "cost" : 50
       }
)

drinks.insert_one(
        {
            "id": 25,
            "name": "Black Russian",
            "drink_type": "mixed",
            "image": "dirty_martini.png",
            "recipe": [
                {
                    "type": "Vodka",
                    "flavor": None,
                    "amount": "2 shots"
                },
                {
                    "type": "Coffee liqueur",
                    "flavor": None,
                    "amount": "1.5 shots"
                }
                            ],
            "available": True,
            "times_ordered" : 0,
            "cost" : 75
       }
)

drinks.insert_one(
        {
            "id": 26,
            "name": "Grasshopper TODO Blended?",
            "drink_type": "mixed",
            "image": "dirty_martini.png",
            "recipe": [
                {
                    "type": "Mint cream",
                    "flavor": None,
                    "amount": "1.5 shots"
                },
                {
                    "type": "Creme de cacao",
                    "flavor": None,
                    "amount": "1.5 shots"
                },
                {
                    "type": "Fresh cream",
                    "flavor": None,
                    "amount": "1 shot"
                }
                            ],
            "available": True,
            "times_ordered" : 0,
            "cost" : 50
       }
)

drinks.insert_one(
        {
            "id": 27,
            "name": "B-52",
            "drink_type": "part",
            "image": "dirty_martini.png",
            "recipe": [
                {
                    "type": "Kahlua",
                    "flavor": None,
                    "amount": "1 part"
                },
                {
                    "type": "Bailey's",
                    "flavor": None,
                    "amount": "1 part"
                },
                {
                    "type": "Brandy",
                    "flavor": None,
                    "amount": "1 part"
                }
                            ],
            "available": True,
            "times_ordered" : 0,
            "cost" : 75
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
            "username" : "bartender",
            "password" : generate_password_hash("bartender"),
            "credits" : 1000000,
            "roles" : [ "admin" ],
            "drinks_ordered" : 0
        }
)
users.insert_one(
        {
            "username" : "user",
            "password" : generate_password_hash("user"),
            "credits" : 1000,
            "roles" : [ "user" ],
            "drinks_ordered" : 0
        }
)
