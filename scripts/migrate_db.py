#! /usr/bin/python
import time
from pymongo import MongoClient, ASCENDING
from werkzeug.security import generate_password_hash
# TODO make usernames unique


client = MongoClient()
db = client.ChambordPi

drinks = db.Drinks
alcohol = db.Alchohol
users = db.Users
orders = db.Orders
mixers = db.Mixers
beer = db.Beer
ingredients = db.Ingredients

all_ing = ingredients.find()
for ing in all_ing:
    if 'bottles' in ing:
        ingredients.delete_one(ing)
        real_ing = {'measure':'bottles', 'cost':ing['cost'], 'available':ing['available'],
                'stock':ing['bottles'], 'name':ing['name'], 'ingredient_class':ing['class'],
                'ingredient_type':ing['type'], 'flavor':ing['flavor'],
                'times_ordered':ing['times_ordered'], '_id':ing['_id']}
        ingredients.insert_one(real_ing)

all_drinks = drinks.find()
for drink in drinks:
    if 'id' in drink:
        drinks.delete_one(drink)
        real_drink = {'_id':drink['_id'], 'available':drink['available'], 'cost':drink['cost'],
                'name':drink['name'], 'times_ordered':drink['times_ordered'],
                'recipe':drink['recipe'], 'image':drink['image'], 'drink_type':drink['type'],
                'drink_id':drink['id']}
        drinks.insert_one(drink)

all_orders = orders.find()
for order in all_orders:
    orders.delete(order)
