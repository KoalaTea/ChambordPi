from werkzeug.security import check_password_hash
from .db import db
from . import lm

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

class User():

    def __init__(self, user_json):
        self.username = user_json['username']
        self.credits = user_json['credits']
        self.roles = user_json['roles']

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

    def purchase(self, credits):
        #look up how to lock the database
        self.credits -= credits
        db.Users.update({
            'username': self.username
        },{
            '$set': {'credits': existing - credits }
        }, upsert=False)


    @staticmethod
    def validate_login(password_hash, password):
        return check_password_hash(password_hash, password)
