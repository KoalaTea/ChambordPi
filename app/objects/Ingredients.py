from flask.ext.mongoalchemy import MongoAlchemy

class Ingredient(db.Document):
    available = db.BoolField()
    cost = db.IntField()
    stock = db.IntField()
    measure = db.StringField()
    name = db.StringField()
    obj_class = db.StringField()
    obj_type = db.StringField()
    flavor = db.StringField()
