from ..db import ingredientsCol as Ingredients
import mixers
import alchohols

from bson import ObjectId

class Ingredient(Document):
    def __init__(self, _id, doc=None):
        self.identifier = {'_id', ObjectId(str(_id))}
        if doc is None:
            self.doc = None
            self.force_update()
        else:
            self.doc = doc

    @staticmethod
    def update_total(ammount):
        #add/remove bottles
        pass

    @staticmethod
    def get_available():
        return self.get({'available':True})

    @staticmethod
    def get(search=None):
        ingredient_list = []
        for i in Document.get('Ingredients', search):
            if i['class'] == "mixer":
                ingredient_list.append(mixers.Mixer(i['_id']), i)
            elif i['class'] == "alchohol":
                ingredient_list.append(alchohols.Alchohol(i['_id']), i)
        return ingredient_list
