from .db import db
import time
from IPython import embed

def create_order(user, drink, instructions):
    resp = db.Orders.insert_one({'name': drink.name, 'cost': drink.cost,
        'drink_type': drink.drink_type, 'recipe': drink.recipe, 'image': drink.image,
        'time_ordered': int(time.time()), 'user': user.username,
        'instructions': instructions, 'status': 'queued'})
    print('db/order_db.create_order embed')
    embed()

def cancel_order(order):
    db.Orders.delete_one({'_id': order._id})

def update_order_status(order, status):
    db.Orders.update_one({'_id': order._id}, {'$set': {'status': status}})
