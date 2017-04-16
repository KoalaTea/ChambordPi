from ..db import drinksCol as Drinks

from bson import ObjectId

class Drink(object):
    def __init__(self, _id, doc=None):
        available = doc.get('available', None)
        cost = doc.get('cost', None)
        name = doc.get('name', None)
        times_ordered = doc.get('times_ordered', 0)
        recipe = doc.get('recipe', None)
        image = doc.get('image', None)
        drink_type = doc.get('type', None)
        drink_id = doc.get('id', None) #Do I Need this?

        drink_doc = {
                'available': available,
                'cost': cost,
                'name': name,
                'times_ordered': times_ordered,
                'recipe': recipe,
                'image': image,
                'type': drink_type,
                'id': drink_id
        }

        super(Drink, self).__init__('Drinks', drink_doc)



    @staticmethod
    def create_drink(name, drink_type, recipe, cost=None, image=None):
        new_drink = Drink({'name': name, 'type': drink_type, 'recipe': recipe, 'cost': cost, 'image': image})
        new_drink.commit()
        return new_drink

    @staticmethod
    def get_available():
        return self.get({'available':True})

    @staticmethod
    def get(search={})
        return [Drink(d) for d in Document.get('Drinks', search)]
