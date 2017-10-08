from app.db import db

def completed_order(order):
    db.db_obj.PastOrders.insert_one()

def remove_credits(credits):
    pass
