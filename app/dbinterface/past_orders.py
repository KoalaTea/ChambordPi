from ..db import pastOrdersCol as PastOrders

from bson import ObjectId

class PastOrder(object):
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
    def user(self):
        return self.doc.get('user')

    @property
    def status(self):
        return self.doc.get('status')

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
    def instructions(self):
        return self.doc.get('instructions')

    @property
    def image(self):
        return self.doc.get('image')

    @property
    def timeOrdered(self):
        return self.doc.get('timeOrdered')

    @property
    def type(self):
        return self.doc.get('type')

    def force_update():
        self.doc = PastOrders.find_one(self.identifier)
        return self.doc is not None

    @staticmethod
    def create_order(drink, username, instructions):
        Orders.insert_one(
            {
                "name": drink['name'],
                "cost": drink['cost'],
                "type": drink['type'],
                "recipe": drink['recipe'],
                "image": drink['image'],
                "timeOrdered": int(time.time()),
                "user": username,
                "instructions": instructions,
                "status": "queued"
            }
        )

    @staticmethod
    def get(search={})
        return [PastOrder(p['_id'], p) for p in PastOrders.find(search)]
