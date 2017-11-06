from ..db import drink_db
from app import the_real_db as db

def create_drink(name, recipe, drink_type):
    drink.Drink(name=name, cost=25, times_ordered=0, recipe=recipe, image='dirty_martini.png',
            drink_type=drink_type) # TODO need drink id....
    # check if available
    drink.commit()

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
