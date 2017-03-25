import mixers
from ..db import ingredientsCol as Ingredients

class Alchohol(mixers.Mixer):
    @property
    def flavor():
        return self.doc.get('flavor')

    @property
    def alchohol():
        return self.doc.get('alchohol')

    @property
    def cost():
        return self.doc.get('cost')

    @staticmethod
    def get(search={}):
        search['type'] = 'alchohol'
        return [Alchohol[a['_id'], a] for a in Ingredients.find(search)]
