from ..db import drink_db

class Drink(object):
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

    def purchase():
        drink_db.purchase(self._id)
        #need to import and update db
        #import session from main and create drink order
