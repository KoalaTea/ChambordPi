from document import Document
import time

from bson import ObjectId

class Order(Document):
    def __init__(self, doc):
        user = doc.get('user', None)
        status = doc.get('status', 'Whatever default is')
        cost = doc.get('cost', None)
        name = doc.get('name', None)
        recipe = doc.get('recipe', None)
        image = doc.get('image', None)
        instructions = doc.get('instructions', None)
        order_type = doc.get('type', None)
        time_ordered = time.time()

        #all the default checks

        order_doc = {
            'user': user,
            'status': status,
            'cost': cost,
            'name': name,
            'recipe': recipe,
            'image': image,
            'instructions': instructions,
            'type': order_type,
            'time_ordered': time_ordered
        }

        super(Order, self).__init__('Orders', order_doc)


    def update_order(self):
        #move state of order along
        if self.status == 'queued':
            self.status = "inprogress"
        elif self.status == 'inprogress':
            self.status = "ready"
        elif self.status == 'ready':
            self.status = 'complete'
            PastOrder.create_past_order(doc)
            del(self._id)
            Users.complete_drink()
            self.delete()
            #del(order['_id'])`

    def cancel_order(drink):
        self.status = 'cancelled'
        PastOrder.create(self.doc)
        #TODO Does not seem right
        self.delete()

    @staticmethod
    def create_order(drink, username, instructions):
        order = drink.doc
        order['user'] = username
        order['instructions'] = instructions
        new_order = Order(order)
        new_order.commit()
        return new_order

    @staticmethod
    def get_order(order_id):
        #if order =?
        order = Order(Document.get('Orders', {'_id': ObjectId(order_id)}))
        if order:
            return order

    @staticmethod
    def get(search={})
        return [Order(o) for o in Document.get('Orders', search)]
