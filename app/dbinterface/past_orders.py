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

    @staticmethod
    def create(drink, username, instructions):
        pass

    @staticmethod
    def get(search={})
        return [PastOrder(p) for p in Document.get('PastOrders', search)]
