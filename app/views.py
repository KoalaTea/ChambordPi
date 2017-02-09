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

# index
#   the main page
#
# returns
#   template of main page
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

# login
#   login page
#
# data
#   username    - the username
#   password    - the password
#
# returns
#   login stuff if successful and redirect to index or flashed failed message if unsuccessful
@app.route("/login", methods=["POST", "GET"])
@app.route("/signin", methods=["POST", "GET"])
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

# logout
#   logour page destroys session
#
# data
#   login information
#
# returns
#   cleared session and redirect to index
@app.route("/logout")
@app.route("/signout")
def logout():
    logout_user()
    return redirect('/index')

# list_alchohol
#   lists all available alchohols
#
# returns
#   alchohol template which has all alchohols available
@app.route("/list_alchohol", methods=["GET", "POST"])
def list_alchohol():
    return render_template('alchohol.html', title='Alchohol', user=user, alchohol_list=db.Alchohol.find())

# add_alchohol
#   will add bottles to an alchohol that exists, or add the alchohol to the list if it does not exist
#
# data
#   alchohol    {
#               type    - alchohol type
#               name    - brand name
#               flavor  - flavor of alchohol (None if just the alchohol)
#               bottles - number of bottles being added
#               }
#
# Returns
#   the new alchohol database entry or empty set if failed
@app.route("/add_alchohol", methods=["POST"])
@bartender_required
def add_alchohol():
    data = request.get_json()
    if set(data.keys()) == set(["type","name","flavor","bottles"]):
         current_alchohol = db.Alchohol.find({"type": data["type"], "name", data["name"], "flavor":data["flavor"])
        if(current_alchohol is None):
            db.Alchohol.insert_one(data)
        # update to set bottles += bottles added
        new_alchohol = db.Alchohol.find(data)
        return new_alchohol
    return "{}"

# remove_alchohol
#   will add bottles to an alchohol that exists, or add the alchohol to the list if it does not exist
#
# data
#   alchohol    {
#               type    - alchohol type
#               name    - brand name
#               flavor  - flavor of alchohol (None if just the alchohol)
#               bottles - number of bottles being removed
#               }
#
# Returns
#   the new alchohol database entry or empty set if failed
@app.route("/remove_alchohol", methods=["POST"])
@bartender_required
def remove_alchohol():
    data = request.get_json()
    if(set(data.keys()) == set(["type","name","flavor","bottles"])):
        print("works")
        current_alchohol = db.Alchohol.find({"type": data["type"], "name": data["name"], "flavor":data["flavor"])
        if(current_alchohol is None or current_alchohol["bottles"] == 0 or current_alchohol["bottles"] > data["bottles"]):
            # raise issue
            return "{}"
        # update to set bottles -= bottles added
        new_alchohol = db.Alchohol.find(data)
        return new_alchohol
    return "{}"

# list_drinks
#   lists all drink recipes in the database
#
# returns
#   drinks template with all recorded drinks
@app.route("/list_drinks", methods=["GET", "POST"])
def list_drinks():
    return render_template('drinks.html', title='All Drinks', user=user, drinks=db.Drinks.find())

# menu
#   lists all available drinks based on alchohol currently in stock
#
# returns
#   menu template with only available drinks
@app.route("/menu", methods=["GET"])
def menu():
    return render_template('menu.html', title='Menu', user=user, drinks=db.Drinks.find({"available" : True}))

# order_drink
#   page to order drinks from
#
# data
#   drink   {
#           name    - name of drink
#           type    - type of drink (shot/mixed/on the rocks)
#           recipe  {
#                   type    - type of alchohol
#                   ammount - ammount to use
#                   }
#           }
#   user    - the user logged in
#
# returns
#   ... TODO think about money and other stuff for fails
@app.route("/order_drink", methods=["POST"])
@login_required
def order_drink():
    #TODO money things
    data = request.get_json()
    if(set(data.keys()) == set(["name"])):
        the_drink = db.Drinks.find(data)
        if(the_drink is not None):
        db.Orders.insert_one({"drink": {"name": the_drink["name"], "type": the_drink["type"], "recipe": the_drink["recipe"]}, "user": current_username.username})
            return db.Orders.find("user", current_user.username)
    return "{}"

# orders
#   view all orders, must be bartender or admin
#
# returns
#   orders template with all current orders listed
#
# TODO verify correct ordering
@app.route("/orders", methods=["GET", "POST"])
@login_required
@bartender_required
def orders():
    orders = db.Orders.find()
    return render_template('orders.html', title='Orders', user=user, orders=orders)

# load_user
#   sets things up for loading a user since we use mongo instead of sqllite
#
# returns
#   User object of the user from the database
@lm.user_loader
def load_user(username):
    u = db.Users.find_one({"username" : username})
    if not u:
        return None
    return User(u)
