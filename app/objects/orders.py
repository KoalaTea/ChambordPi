from ..db import order_db
from ..db import user_db
from app import the_real_db as db

class Order(db.Document):
    username = db.StringField()
    status = db.StringField()
    cost = db.IntField()
    recipe = db.DictField()
    name = db.StringField()
    image = db.StringField()
    instructions = db.StringField()
    order_type = db.StringField()
    times_ordered = db.IntField()
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
            order_db.delete_order(self)
            #TODO status = cancelled; make pastorder
            user_db.cancel_order(self)
        else:
            pass

    def update_order(self):
        if self.status == 'queued':
            order_db.update_order_status(self, 'inprogress')
        elif self.status == 'inprogress':
            order_db.update_order_status(self, 'ready')
        elif self.statys == 'ready':
            order_db.delete(self)
            self.status = 'complete'
            #TODO create past order unique new _id
            user_db.complete_order(self)
        #compare statuses and update based off of that
        pass

    def complete_order():
        # TODO need to do the entire pastorder db
        #import session make new past order
        order_db.delete_order(self)
