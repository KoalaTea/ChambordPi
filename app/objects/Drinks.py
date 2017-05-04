from flask.ext.mongoalchemy import MongoAlchemy

class Drink(db.Document):
    name = db.StringField()
