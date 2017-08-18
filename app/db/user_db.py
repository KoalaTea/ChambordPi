from app.db import db
from werkzeug.security import generate_password_hash
from IPython import embed

def order_drink(user, drink):
    resp = db.db_obj.Users.update_one({'username': user.username},
            {'$inc': {'credits': -drink.cost, 'drinks_ordered': 1}})
    print('db/user_db.order_drink embed')
    embed()

def create_user(username, password):
    resp = db.db_obj.Users.insert_one({'username': username,
        'password': generate_password_hash(password), 'credits': 0, 'roles': ['user'],
        'drinks_ordered': 0})

def cancel_order(order):
    resp = db.db_obj.Users.update_one({'username': order.username},
            {'$inc': {'credits': order.cost, 'drinks_ordered': -1}})

def complete_order(order):
    db.db_obj.Users.update_one({'username': order.username}, {'$inc': {'drinks_ordered': -1}})

def remove_credits(credits):
    pass
