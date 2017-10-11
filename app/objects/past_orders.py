from ..db import past_order_db
from app import the_real_db as db

class PastOrder(db.Document):
    status = db.StringField()
    name = db.StringField()
    recipe = db.DictField()
    cost = db.IntField()
    user = db.StringField()
    order_type = db.StringField()
    times_ordered = db.IntField()
    insructions = db.StringField()
    '''
    def __init__(self, fields_dict):
        self.status = fields_dict['status']
        self.name = fields_dict['name']
        self.recipe = fields_dict['recipe'] #maybe remove this, does it matter in pastorder?
        self.cost = fields_dict['cost']
        self.user = fields_dict['user']
        self.order_type = fields_dict['order_type']
        self.time_ordered = fields_dict['times_ordered']
        self.instructions = fields_dict['instructions']
    '''
