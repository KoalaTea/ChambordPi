import ingredients
from ..db import ingredientsCol as Ingredients

class Mixer(ingredients.Ingredient):

    @property
    def bottles(self):
        return self.doc.get('bottles')

    @staticmethod
    def get(search={}):
        search['type'] = 'mixer'
        return [Mixer(m['_id'], m) for m in Ingredients.find(search)]
