from mongoalchemy.document import Document
from mongoalchemy.fields import *

class PastOrder(Document):
    status = StringField()
    name = StringField()
    recipe = AnythingField() #maybe remove this, does it matter in pastorder
    cost = IntField()
    user = StringField()
    obj_type = StringField()
    time_orders = IntField()
    instructions = StringField()
