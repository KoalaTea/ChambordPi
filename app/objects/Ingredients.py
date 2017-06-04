from mongoalchemy.document import Document
from mongoalchemy.fields import *

class Ingredient(Document):
    available = BoolField()
    cost = IntField()
    stock = IntField()
    measure = StringField()
    name = StringField()
    obj_class = StringField()
    obj_type = StringField()
    flavor = StringField()
    times_ordered = IntField()

    def add(self, added_stock):
        self.stock.inc(stock, added_stock).execute()

    def remove(self, removed_stock):
        self.stock.inc(stock, -removed_stock).execute()
