from werkzeug.security import check_password_hash
from app.db import user_db
from app.db import order_db
from app import lm
#import ..db.user_db as user_db
#import ..db.order_db as order_db

# load_user
#   sets things up for loading a user since we use mongo instead of sqllite
#
# returns
#   User object of the user from the database
@lm.user_loader
def load_user(username):
    u = db.Users.find_one({"username": username})
    if not u:
        return None
    return User(u)

class User(object):

    def __init__(self, user_json):
        self.username = user_json['username']
        self.credits = user_json['credits']
        self.roles = user_json['roles']
        self.drinks_ordered = user_json['drinks_ordered']

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
        db.Users.update({
            'username': self.username
        },{
            '$set': {'credits': existing - credits }
        }, upsert=False)


    @staticmethod
    def validate_login(password_hash, password):
        return check_password_hash(password_hash, password)
