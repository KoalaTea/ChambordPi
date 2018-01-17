from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from collections import namedtuple
import time
from app import db
from app.objects import orders

def create_user(username, password):
    if User.objects.get(username=username):
        return None
    password_hash = generate_password_hash(password)
    user = User(username, password_hash, ['user'], 0, 0)
    user.commit()
    return user

class User(db.Document):
    username = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    roles = db.ListField(db.StringField())
    credits = db.IntField()
    drinks_ordered = db.IntField()
    '''
    def __init__(self, user_json):
        self.username = user_json['username']
        self.password = user_json['password']
        self.credits = user_json['credits']
        self.roles = user_json['roles']
        self.drinks_ordered = user_json['drinks_ordered']
    '''

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymouse(self):
        return False

    def get_id(self):
        return self.username

    def is_role(self, role):
        return(role in self.roles)

    def order_drink(self, drink, instructions):
        #look up how to lock the database
        if self.credits >= drink.cost:
            self.credits -= drink.cost
            self.drinks_ordered += 1
            self.save()
            print('credits updated for {}'.format(self.username))
            #hacky solution to recipe being a list TODO come back to this
            order = orders.Order(username=self.username, status='queued', cost=drink.cost,
                    recipe=drink.recipe, name=drink.name, image=drink.image,
                    instructions=instructions, order_type=drink.drink_type,
                    time_ordered=int(time.time()))
            order.save()
            drink.purchase()
            print('order created')
        else:
            print('user {} does not have enough credits to order {}').format(self.username, drink.name)

    def order_custom_drink(self, drink, instructions):
        #look up how to lock the database
        if self.credits >= CUSTOM_DRINK_COST:
            self.credits -= drink.cost
            self.drinks_ordered += 1
            self.save()
            print('credits updated for {}'.format(self.username))

            order = orders.Order(username=self.username, status='queued', cost=CUSTOM_DRINK_COST,
                    recipe=drink.recipe, name=drink.name, image=drink.image,
                    instructions=instructions, order_type=drink.drink_type,
                    time_ordered=int(time.time()))
            order.save()
            print('order created')
            return '{"status": "completed"}'
        else:
            print('user {} does not have enough credits to order {}').format(self.username, drink.name)
            return '{"status": "failed - not enough credits"}'

    def cancel_order(self, order):
        self.credits += order.cost
        self.drinks_ordered -= 1
        self.save()

    @staticmethod
    def validate_login(password_hash, password):
        return check_password_hash(password_hash, password)

'''
@lm.user_loader
def load_user(username):
    u = users.User.objects.get(username=username)
    if not u:
        return None
    return u
'''
