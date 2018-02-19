from flask import Flask
from pymongo import MongoClient
from flask_mongoengine import MongoEngine

#app = Flask(__name__)
#app.config.from_object('config')
#app.config['MONGODB_SETTINGS'] = {'db': 'ChambordPi'}
#db = MongoEngine(app)
db = MongoEngine()

from flask_login import LoginManager

lm = LoginManager()
lm.session_protection = 'strong'
lm.login_view = 'auth.login'
#lm.init_app(app)


def create_app(**config_overrides):
    app = Flask(__name__)
    app.config.from_object('config')
    app.config['MONGODB_SETTINGS'] = {'db': 'ChambordPi'}
    from app.auth import auth as auth_blueprint
    from app.bartender import bartender as bartender_blueprint
    from app.admin import admin as admin_blueprint
    from app.views import views as views_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(bartender_blueprint)
    app.register_blueprint(admin_blueprint, url_prefix="/admin")
    app.register_blueprint(views_blueprint)
    app.config.update(config_overrides)
    lm.init_app(app)
    db.init_app(app)
    return app

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
