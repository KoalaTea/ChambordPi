import json
import time
from flask import render_template, flash, redirect, request, url_for
#from app import app
from bson.objectid import ObjectId
from werkzeug.security import check_password_hash
from flask_login import login_required, login_user, logout_user, current_user
from app.decorators import bartender_required, admin_required
from pymongo import MongoClient

from app.objects import drinks
from app.objects import orders
from app.objects import ingredients
from app.objects import users

from flask import Blueprint
views = Blueprint('views', __name__)

#TODO move current_user to using the objects version

CURRENT_STAT_FILE = 1
CUSTOM_COST=150

# TODO:
#   set all pages to check for authentication and if none - guest@Hackerbar
#   metrics
#   times
#   logging

# index
#   the main page
#
# returns
#   template of main page
@views.route("/")
@views.route("/index")
def index():
    drink_list = [
        {
            'drink_name' : 'Godfather',
            'ingredients' : [ 'half ameretto', 'half scotch whiskey' ]
        },
        {
            'drink_name' : 'temp test',
            'ingredients' : [ 'nothing', 'more nothing' ]
        }
    ]
    return render_template('index.html', title='Home', user=current_user, drinks=drink_list)

# list_drinks
#   lists all drink recipes in the database
#
# returns
#   drinks template with all recorded drinks
@views.route("/list_drinks", methods=["GET", "POST"])
@views.route("/recipes", methods=["GET", "POST"])
def list_drinks():
    drink_list = drinks.Drink.objects()
    return render_template('recipes.html', title='All Drinks', user=current_user, drinks=drink_list)

# menu
#   lists all available drinks based on alchohol currently in stock
#
# returns
#   menu template with only available drinks

@views.route("/menu", methods=["GET"])
def menu():
    drink_list = drinks.Drink.objects(available=True)
    if(current_user.is_authenticated):
        return render_template('menu_auth.html', title='Menu',
                           user=current_user,
                           credits=get_user_credits(current_user.username),
                           drinks=drink_list)
    else:
         return render_template('menu_unauth.html', title='Menu',
                           drinks=drink_list)

@views.route("/recent_orders")
@login_required
def recent_orders():
    order_list = orders.Order.objects(username=current_user.username)
    return render_template('recent_orders.html',
                           title='Orders',
                           user=current_user,
                           orders=order_list,
                           totaldrinks=get_user_drinks(current_user.username),
                           credits=get_user_credits(current_user.username))

#needs a rethinkg TODO
@views.route('/review_order/<drinkname>')
@login_required
def review_order(drinkname):
    print(drinkname)
    drink = drinks.Drink.objects.get(name=drinkname)
    if drink is not None:
        return render_template('review_order.html', title='Review and Order', user=current_user, drink=drink)
    else:
        return redirect(url_for('menu'))

#Need to test order_drink statistics more, but is backed up in completed orders anyways
@views.route('/order_drink', methods=["POST"])
@login_required
def order_drink():
    postData = dict(request.form)
    drink = drinks.Drink.objects.get(name=postData['drink'][0])
    instructions = postData['instructions'][0]
    if drink is not None:
        current_user.order_drink(drink, instructions)
        # TODO figure out this return incase drink order fails
        # return '{"status": "failed - not enough credits"}'
    return '{"result": "success"}'

@views.route('/cancel_drink', methods=["POST"])
@login_required
def cancel_drink():
    postData = dict(request.form)
    order_id = ObjectId(postData['order'][0])
    order = orders.Order.objects.get(id=order_id)
    if order is not None:
        order.cancel_order()
    return '{"result": "success"}'

@views.route('/custom_drink')
@login_required
def custom_drink():
    ing_objects = ingredients.Ingredient.objects()
    return render_template('custom_drink.html', ingredients=ing_objects)

# TODO
@views.route('/order_custom_drink', methods=["POST"])
@login_required
def order_custom_drink():
    recipe = []
    post_data = dict(request.form)
    print(post_data['recipe[]'])

    for ing in post_data['recipe[]']: #TODO????
        print(ing)
        ingredient = {}
        ingredient['type'] = ing
        ingredient['flavor'] = ''
        ingredient['amount'] = ""
        recipe.append(ingredient)

    return current_user.order_custom_drink({"name": "Custom Drink", "cost": CUSTOM_COST,
                                           "drink_type": "custom", "recipe": recipe,
                                           "image": 'custom_drink.png'},
                                           post_data['instructions'][0])

# TODO wait what is this doing? come back to it later figure out why it is doing things
# I do not seem to understand
# TODO wait this may be done
@views.route("/order_complete", methods=["POST"])
@login_required
@bartender_required
def order_complete():
    data = request.json
    if(set(data.keys()) == set(["_id"])):
        order = orders.Order.objects.get(id=ObjectId(data["_id"]))
        if order is not None:
            order.complete_order()
    order_list = orders.Order.objects()
    return render_template('current_orders.html', title='Orders', user=current_user, orders=orders)

# do not really care about these anymore
def get_user_credits(username):
    user = users.User.objects.get(username=username)
    return user.credits
def get_user_drinks(username):
    user = users.User.objects.get(username=username)
    return user.drinks_ordered
