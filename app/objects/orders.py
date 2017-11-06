from ..db import order_db
from ..db import user_db
from app import the_real_db as db
from app.objects import users

def create_order(drink, user, instructions):
    order = Order(username=user.username, status='queued', cost=drink.cost, recipe=drink.recipe,
            name=drink.name, image=drink.image, instructions=instructions) # TODO add time and order_type


class Order(db.Document):
    username = db.StringField()
    status = db.StringField()
    cost = db.IntField()
    recipe = db.DictField()
    name = db.StringField()
    image = db.StringField()
    instructions = db.StringField()
    order_type = db.StringField()
    time_ordered = db.IntField()
    '''
    def __init__(self, fields_dict):
        _id = fields_dict['_id']
        username = fields_dict['username']
        status = fields_dict['status']
        cost = fields_dict['cost']
        recipe = fields_dict['recipe']
        name = fields_dict['name']
        image = fields_dict['image']
        instructions = fields_dict['instructions']
        order_type = fields_dict['order_type']
        time_ordered = fields_dict['times_ordered'] #maybe/maybe not meant for here
    '''

    def cancel_order(self):
        if self.status.lower() == 'queued':
            #TODO status = cancelled; make pastorder
            users.User.get(username=self.username).cancel_order(self)
            self.delete()

    def update_order(self):
        if self.status == 'queued':
            self.status = 'inprogress'
        elif self.status == 'inprogress':
            self.status = 'ready'
        elif self.status == 'ready':
            order_db.delete(self)
            self.status = 'complete'
            #TODO create past order unique new _id
            user_db.complete_order(self)
            return
        self.save()

    def complete_order():
        # TODO need to do the entire pastorder db
        #import session make new past order
        order_db.delete_order(self)
