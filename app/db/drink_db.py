from app.db import db

def set_unavailable(_id):
    db.db_obj.Users.update_one({'_id': _id}, {'$set': {'available': False}})

def remove_credits(credits):
    pass
