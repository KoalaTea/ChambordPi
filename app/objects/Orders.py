from flask.mongo.mongoalchemy import MongoAlchemy

class Order(db.Document):
    user = db.StringField()
    status = db.StringField()
    cost = db.IntField()
    recipe = db.AnythingField()
    image = db.StringField()
    instructions = db.StringField()
    obj_type = db.StringField()
    time_ordered = db.IntField()
