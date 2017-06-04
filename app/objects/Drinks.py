from mongoalchemy.document import Document
from mongoalchemy.fields import *

class Drink(Document):
    available = BoolField()
    cost = IntField()
    name = StringField()
    times_ordered = IntField()
    recipe = AnythingField()
    image = StringField()
    obj_type = StringField()
    drink_id = IntField()

    def purchase():
        self.inc(times_ordered, 1).execute()
        #import session from main and create drink order
        pass
