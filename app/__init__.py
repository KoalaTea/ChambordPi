from flask import Flask
from pymongo import MongoClient
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object('config')
app.config['MONGODB_SETTINGS'] = {'db': 'ChambordPi'}
the_real_db = MongoEngine(app)

from flask_login import LoginManager

lm = LoginManager()
lm.session_protection = 'strong'
lm.login_view = 'auth.login'
lm.init_app(app)



from app.auth import auth as auth_blueprint
from app.bartender import bartender as bartender_blueprint
from app.admin import admin as admin_blueprint
app.register_blueprint(auth_blueprint, url_prefix="/auth")
app.register_blueprint(bartender_blueprint, url_prefix="/bartender")
app.register_blueprint(admin_blueprint, url_prefix="/admin")


def create_app(config_name):
    from app.auth import auth as auth_blueprint
    from app.bartender import bartender as bartender_blueprint
    from app.admin import admin as admin_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(bartender_blueprint)
    app.register_blueprint(admin_blueprint, url_prefix="/admin")
    lm = LoginManager()
    lm.session_protection = 'strong'
    lm.login_view = 'auth.login'
    lm.init_app(app)
    return app

from app.db import db_getters
from app.objects import users
# load_user
#   sets things up for loading a user since we use mongo instead of sqllite
#
# returns
#   User object of the user from the database
@lm.user_loader
def load_user(username):
    u = users.User.objects.get(username=username)
    if not u:
        return None
    return u

from app import views
