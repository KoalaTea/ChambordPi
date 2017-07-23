from ..db import ingredient_db

class Ingredient(object):
    def __init__(self, fields_dict)
        self.available = fields_dict['available']
        self.cost =  fields_dict['cost']
        self.stock = fields_dict['stock']
        self.measure = fields_dict['measure']
        self.name = fields_dict['name']
        self.ingredient_class = fields_dict['ingredient_class']
        self.ingredient_type = fields_dict['ingredient_type']
        self.flavor = fields_dict['flavor']
        self.times_ordered = fields_dict['times_ordered']

    def add(self, added_stock):
        ingredient_db.add_stock(added_stock)

    def remove(self, removed_stock):
        ingredient_db.remove_stock(removed_stock)
