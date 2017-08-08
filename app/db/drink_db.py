from .db import db

def set_unavailable(_id):
    db.Users.update_one({'_id': _id}, {'$set': {'available': False}})

def remove_credits(credits):
    pass
