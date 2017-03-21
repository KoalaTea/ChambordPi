from ..db import drinksCol as Drinks

from bson import ObjectId

class Drink(object):
    def __init__(self, _id, doc=None):
        self.identifier = {'_id', ObjectId(str(_id))}
        if doc is None:
            self.doc = None
            self.force_update()
        else:
            self.doc = doc

    @property
    def _id(self):
        return self.doc.get('_id', None)

    @property
    def available(self):
        return self.doc.get('available')

    @property
    def times_ordered(self):
        return self.doc.get('times_ordered')

    @property
    def cost(self):
        return self.doc.get('cost')

    @property
    def name(self):
        return self.doc.get('name')

    @property
    def recipe(self):
        return self.doc.get('recipe')

    @property
    def type(self):
        return self.doc.get('type')

    @property
    def image(self):
        return self.doc.get('image')

    def force_update():
        self.doc = Drinks.find_one(self.identifier)
        return self.doc is not None

    @staticmethod
    def get_available():
        return self.get({'available':True})

    @staticmethod
    def get(search={})
        return [Drink(o['_id'], o) for o in Drinkss.find(search)]
