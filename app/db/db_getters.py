from .db import db
from ..objects.drinks import Drink
from ..objects.orders import Order
from ..objects.past_orders import PastOrder
from ..object.ingredients import Ingredient

def get_drinks(**kwargs):
    mongo_drinks = db.Drinks.find(**kwargs)
    drink_objects = [Drink(mongo_drink) for mongo_drink in mongo_drinks]
    return drink_objects

def get_available_drinks():
    return get_drinks({'available': True})

def get_drink(name):
    drink_mongo = db.Drinks.find_one({'name': name})
    return Drink(drink_mongo)

def get_orders(**kwargs):
    mongo_orders = db.Orders.find(**kwargs)
    order_objects = [Order(mongo_order) for mongo_order in mongo_orders]
    return orders

def get_order(order_id):
    mongo_order = db.Orders.find_one({'_id': order_id})
    return Order(mongo_order)

def get_past_orders(**kwargs):
    mongo_past_orders = db.PastOrders.find(**kwargs)
    past_order_objects = [PastOrder(mongo_past_order) for past_order in mongo_past_orders]
    return past_order_objects

def get_ingredients(**kwargs):
    mongo_ingredients = db.Ingredients.find(**kwargs)
    ingredient_objects = [Ingredient(mongo_ingredient) for mongo_ingredient in mongo_ingredients]
    return ingredient_objects

def get_available_ingredients():
    return get_ingredients({'available': True})

def get_users():
    pass #probs not gonan be a function
