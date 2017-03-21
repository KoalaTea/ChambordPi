from ..db import ingredientsCol as Ingredients
import mixers
import alchohols

from bson import ObjectId

class Ingredient(object):
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
    def bottles(self):
        return self.doc.get('bottles')

    @property
    def type(self):
        return self.doc.get('type')

    @property
    def name(self):
        return self.doc.get('name')

    def force_update():
        self.doc = Ingredients.find_one(self.identifier)
        return self.doc is not None

    @staticmethod
    def get_available():
        return self.get({'available':True})

    @staticmethod
    def get(search={}):
        ingredient_list = []
        for i in Ingredients.find(search):
            if i['class'] == "mixer":
                ingredient_list.append(mixers.Mixer(i['_id']), i)
            elif i['class'] == "alchohol":
                ingredient_list.append(alchohols.Alchohol(i['_id']), i)
        return ingredient_list
