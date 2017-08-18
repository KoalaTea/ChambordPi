from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object('config')


from flask_login import LoginManager

lm = LoginManager()
lm.session_protection = 'strong'
lm.login_view = 'auth.login'
lm.init_app(app)



from auth import auth as auth_blueprint
from bartender import bartender as bartender_blueprint
from admin import admin as admin_blueprint
app.register_blueprint(auth_blueprint, url_prefix="/auth")
app.register_blueprint(bartender_blueprint, url_prefix="/bartender")
app.register_blueprint(admin_blueprint, url_prefix="/admin")


def create_app(config_name):
    from auth import auth as auth_blueprint
    from bartender import bartender as bartender_blueprint
    from admin import admin as admin_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(bartender_blueprint)
    app.register_blueprint(admin_blueprint, url_prefix="/admin")
    lm = LoginManager()
    lm.session_protection = 'strong'
    lm.login_view = 'auth.login'
    lm.init_app(app)
    return app

from app.db import db_getters
# load_user
#   sets things up for loading a user since we use mongo instead of sqllite
#
# returns
#   User object of the user from the database
@lm.user_loader
def load_user(username):
    u = db_getters.get_user(username)
    if not u:
        return None
    return u

from app import views
