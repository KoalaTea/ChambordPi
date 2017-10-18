from app.db import ingredient_db
from app import the_real_db as db

class Ingredient(db.Document):
    name = db.StringField()
    cost = db.IntField()
    measure = db.StringField()
    stock = db.IntField()
    ingredient_class = db.StringField()
    ingredient_type = db.StringField()
    available = db.BooleanField()
    flavor = db.StringField()
    times_ordered = db.IntField()
    '''
    def __init__(self, fields_dict):
        self.available = fields_dict['available']
        self.cost =  fields_dict['cost']
        self.stock = fields_dict['stock']
        self.measure = fields_dict['measure']
        self.name = fields_dict['name']
        self.ingredient_class = fields_dict['ingredient_class']
        self.ingredient_type = fields_dict['ingredient_type']
        self.flavor = fields_dict['flavor']
        self.times_ordered = fields_dict['times_ordered']
    '''

    def add(self, added_stock):
        self.stock += added_stock
        self.save()

    def remove(self, removed_stock):
        self.stock -= removed_stock
        self.save()
