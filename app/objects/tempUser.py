from flask.mongo.mongoalchemy import MongoAlchemy

class user(db.Document):
    username = db.StringField()
    password = db.StringField()
    roles = db.AnyField()
    drinksOrdered = db.IntField()
    credits = db.IntField()
