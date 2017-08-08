from .db import db
from IPython import embed

def order_drink(user, drink):
    resp = db.Users.update_one({'username': user.username},
            {'$inc': {'credits': -drink.cost, 'drinks_ordered': 1}})
    print('db/user_db.order_drink embed')
    embed()


def cancel_order(order):
    resp = db.Users.update_one({'username': order.username},
            {'$inc': {'credits': order.cost, 'drinks_ordered': -1}})

def complete_order(order):
    db.Users.update_one({'username': order.username}, {'$inc': {'drinks_ordered': -1}})

def remove_credits(credits):
    pass
