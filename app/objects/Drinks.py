from flask.ext.mongoalchemy import MongoAlchemy

class Drink(db.Document):
    available = db.BoolField()
    cost = db.IntField()
    name = db.StringField()
    times_ordered = db.IntField()
    recipe = AnythingField()
    image = db.StringField()
    obj_type = db.StringField()
    drink_id = db.IntField()
