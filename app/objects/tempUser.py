from mongoalchemy.document import Document
from mongoalchemy.fields import *

class user(Document):
    username = StringField()
    password = StringField()
    roles = AnyField()
    drinksOrdered = IntField()
    credits = IntField()
