from document import Document

from bson import ObjectId

class Order(Document):
    def __init__(self, _id, doc=None):
        self.identifier = {'_id', ObjectId(str(_id))}
        if doc is None:
            self.doc = None
            self.force_update()
        else:
            self.doc = doc

    def force_update():
        self.doc = Orders.find_one(self.identifier)
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
        return [Order(o['_id'], o) for o in Document.get('Orders', search)]
