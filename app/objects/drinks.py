from ..db import drink_db
from app import the_real_db as db
from app.objects import order

class Drink(db.Document):
    name = db.StringField(required=True)
    available = db.BooleanField()
    cost = db.IntField()
    times_ordered = db.IntField()
    recipe = db.DictField(required=True)
    image = db.StringField()
    drink_type = db.StringField()
    drink_id = db.IntField()
    '''
    def __init__(self, fields_dict):
        #TODO actuall make an init
        self._id = fields_dict['_id']
        self.available = fields_dict['available']
        self.cost = fields_dict['cost']
        self.name = fields_dict['name']
        self.times_ordered = fields_dict['times_ordered']
        self.recipe = fields_dict['recipe']
        self.image = fields_dict['image']
        self.drink_type = fields_dict['drink_type']
        self.drink_id = fields_dict['drink_id'] # still don't know if I need this
    '''

    def purchase(self):
        self.times_ordered += 1
        self.save()

    def set_unavailable(self):
        self.available = False
        self.save()
