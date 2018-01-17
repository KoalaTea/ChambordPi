#from ..db import past_order_db
from app import db

class PastOrder(db.Document):
    status = db.StringField()
    name = db.StringField()
    recipe = db.DictField()
    cost = db.IntField()
    username = db.StringField()
    order_type = db.StringField()
    time_ordered = db.IntField()
    insructions = db.StringField()
