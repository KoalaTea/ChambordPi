from werkzeug.security import check_password_hash
from collections import namedtuple
from app.db import user_db
from app.db import order_db
#import ..db.user_db as user_db
#import ..db.order_db as order_db
from app import the_real_db as db

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
            self.credits -= credits
            self.drinks_ordered += 1
            user_db.update(user)
            print('credits updated for {}'.format(username))
            order_db.create_order(self, drink, instructions)
            print('order created')
        else:
            pass
        db.Users.update({'username': self.username},
                {'$set': {'credits': existing - credits }},
                upsert=False)

    def order_custom_drink(self, drink, instructions):
        #look up how to lock the database
        if self.credits >= drink.cost:
            self.credits -= credits
            self.drinks_ordered += 1
            user_db.update(user)
            print('credits updated for {}'.format(username))
            Drink = namedtuple('Drink', ['name', 'cost', 'drink_type', 'recipe', 'image'])
            drink = Drink(drink['name'], drink['cost'], drink['drink_type'], drink['recipe'],
                    drinkt['image'])
            order_db.create_order(self, drink, instructions)
            print('order created')
        else:
            pass
        db.Users.update({'username': self.username},
                {'$set': {'credits': existing - credits }},
                upsert=False)

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
