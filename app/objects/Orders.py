from mongoalchemy.document import Document
from mongoalchemy.fields import *

class Order(Document):
    user = StringField()
    status = StringField()
    cost = IntField()
    recipe = AnythingField()
    name = StringField()
    image = StringField()
    instructions = StringField()
    obj_type = StringField()
    time_ordered = IntField()

    def complete():
        #import session make new past order
        pass
