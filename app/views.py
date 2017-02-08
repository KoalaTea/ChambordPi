from flask import render_template, flash, redirect, request
from app import app, lm
from .forms import LoginForm
from pymongo import MongoClient
from werkzeug.security import check_password_hash
from flask_login import login_required, login_user, logout_user
from .objects import User
from .decorators import bartender_required, admin_required
from .db import db

#client = MongoClient()
#db = client.ChambordPi
user = { "nickname" : "koalatea" }

@app.route("/")
@app.route("/index")
def index():
    user = { "nickname": "koalatea" }
    drinks = [
        {
            'drink_name' : 'Godfather',
            'ingredients' : [ 'half ameretto', 'half scotch whiskey' ]
        },
        {
            'drink_name' : 'temp test',
            'ingredients' : [ 'nothing', 'more nothing' ]
        }
    ]
    return render_template('index.html', title='Home', user=user, drinks=drinks)

@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if(request.method == "POST" and form.validate_on_submit()):
        user = db.Users.find_one({"username": form.username.data})
        if(user is not None and User.validate_login(user['password'], form.password.data)):
            user_obj = User(user)
            login_user(user_obj)
        else:
            flash('Login failed for username="%s" and password="%s"' % (form.username.data, form.password.data))
        flash('Login for username="%s" and password="%s"' % (form.username.data, form.password.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect('/index')

@app.route("/list_alchohol", methods=["GET", "POST"])
def list_alchohol():
    return render_template('alchohol.html', title='Alchohol', user=user, alchohol_list=db.Alchohol.find())

@app.route("/list_drinks", methods=["GET", "POST"])
def list_drinks():
    return render_template('drinks.html', title='All Drinks', user=user, drinks=db.Drinks.find())

@app.route("/menu", methods=["GET", "POST"])
def menu():
    return render_template('drinks.html', title='Menu', user=user, drinks=db.Drinks.find({"available" : True}))

@app.route("/orders", methods=["GET", "POST"])
@login_required
@bartender_required
def orders():
    return "Only bartenders"


@lm.user_loader
def load_user(username):
    u = db.Users.find_one({"username" : username})
    if not u:
        return None
    return User(u)
