#from ..db import order_db
#from ..db import user_db
from app import db
from app.objects import users
from app.objects import past_orders

class Order(db.Document):
    username = db.StringField()
    status = db.StringField()
    cost = db.IntField()
    recipe = db.DictField() # one day move this to using objects through reference (maybe?)
    name = db.StringField()
    image = db.StringField()
    instructions = db.StringField()
    order_type = db.StringField()
    time_ordered = db.IntField()

    def cancel_order(self):
        if self.status.lower() == 'queued':
            #TODO status = cancelled; make pastorder
            past_order = past_orders.PastOrder(status='cancelled', name=self.name,
                                               recipe=self.recipe, cost=self.cost,
                                               username=self.username, order_type=self.order_type,
                                               time_ordered=self.time_ordered,
                                               instructions=self.instructions)
            past_order.save()
            users.User.get(username=self.username).cancel_order(self)
            self.delete()

    def update_order(self):
        if self.status == 'queued':
            self.status = 'inprogress'
        elif self.status == 'inprogress':
            self.status = 'ready'
        elif self.status == 'ready':
            order_db.delete(self)
            past_order = past_orders.PastOrder(status='complete', name=self.name,
                                               recipe=self.recipe, cost=self.cost,
                                               username=self.username, order_type=self.order_type,
                                               time_ordered=self.time_ordered,
                                               instructions=self.instructions)
            past_order.save()
            user_db.complete_order(self)
            self.delete()
            return
        self.save()
