from flask.ext.mongoalchemy import MongoAlchemy

class PastOrder(db.Document):
    status = db.StringField()
    name = db.StringField()
    recipe = db.AnythingField() #maybe remove this, does it matter in pastorder
    cost = db.IntField()
    user = db.StringField()
    obj_type = db.StringField()
    time_orders = db.IntField()
    instructions = db.StringField()
