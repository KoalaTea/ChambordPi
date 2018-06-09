from flask import render_template, flash, redirect, request, url_for
from . import bartender
from pymongo import MongoClient
from bson.objectid import ObjectId
from werkzeug.security import check_password_hash
from flask_login import login_required, login_user, logout_user, current_user
from app.objects.users import User
from app.decorators import bartender_required, admin_required

from app.objects import orders
from app.objects import drinks

import json
import time

CURRENT_STAT_FILE = 1
CUSTOM_COST=150

# TODO:
#   set all pages to check for authentication and if none - guest@Hackerbar
#   metrics
#   times
#   logging
#   cleanup now that blueprints are in use
#   TEST add/remove alchohol

# list_alchohol
#   lists all available alchohols
#
# returns
#   alchohol template which has all alchohols available
@bartender.route("/list_alcohol", methods=["GET", "POST"])
def list_alchohol():
    return render_template('bartender/alchohol.html', title='Alchohol', user=current_user, alchohol_list=db.Alchohol.find())

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
@bartender.route("/add_alcohol", methods=["POST"])
@login_required
@bartender_required
def add_alchohol():
    data = request.get_json()
    if set(data.keys()) == set(["type","name","flavor","bottles"]):
        current_alchohol = db.Alchohol.find({"type": data["type"], "name": data["name"], "flavor":data["flavor"]})
        if(current_alchohol is None):
            db.Alchohol.insert_one(data)
        #TODO update to set bottles += bottles added
        db.Alchohol.update_one({"_id": current_alchohol["_id"]},
            {
                '$inc': {
                    "bottles": data['bottles']
                }
            })
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
@bartender.route("/remove_alcohol", methods=["POST"])
@login_required
@bartender_required
def remove_alchohol():
    data = request.get_json()
    if(set(data.keys()) == set(["type","name","flavor","bottles"])):
        print("works")
        current_alchohol = db.Alchohol.find({"type": data["type"], "name": data["name"], "flavor":data["flavor"]})
        if(current_alchohol is None or current_alchohol["bottles"] == 0 or current_alchohol["bottles"] < data["bottles"]):
            # raise issue
            return "{}"
        #TODO update to set bottles -= bottles added
        db.Alchohol.update_one({"_id": current_alchohol["_id"]},
            {
                '$inc': {
                    "bottles": -data['bottles']
                }
            })
        new_alchohol = db.Alchohol.find(data)
        return new_alchohol
    return "{}"

@bartender.route("/orders", methods=["GET"])
@login_required
@bartender_required
def list_orders():
    order_list = orders.Order.objects()
    #orders = db_getters.get_orders()
    drink_list = drinks.Drink.objects(available=True)
    #drinks = db_getters.get_available_drinks()
    return render_template('bartender/orders.html', title='Bartender', user=current_user,
            orders=order_list, drinks=drink_list)

@bartender.route("/update_order", methods=["POST"])
@login_required
@bartender_required
#TODO delete order and move it to PastOrders on completion
def update_order():
    post_data = dict(request.form)
    order_up = ObjectId(post_data['id'][0])
    status = post_data['status'][0]
    order = orders.Order.get(id=order_up)
    #order = db_getters.get_order(order_up)
    if status.lower() == order.status:
        order.update_order()

    return redirect(url_for('bartender.list_orders'))

@bartender.route("/update_menu", methods=["POST"])
@login_required
@bartender_required
def update_menu():
    data = request.get_json()
    if(set(data.keys()) == set(["type","flavor"])):
        print("works")
        have_more = False
        alchohols = db.Alchohol.find({"type": data["type"], "flavor": data["flavor"]})
        if(alchohols is not None):
            for alchohol in alchohols:
                if(alchohol["bottles"] > 0):
                    have_more = True
            if(have_more):
                #TODO decide on format
                return '{"okay":"cool"}'
            else:
                #drinks = db_getters.get_available_drinks()
                drink_list = drinks.Drink.objects(available=True)
                for drink in drink_list:
                    for ingredient in drink.recipe:
                        if(ingredient["type"] == data["type"] and ingredient["flavor"] == data["flavor"]):
                            #TODO update the drinks availability to false
                            #TODO maybe complete?

                            drink.set_unavailable()
                            return '{"New": "Menu"}'
    return "{}"


@bartender.route("/current_orders", methods=["GET"])
@login_required
@bartender_required
def current_orders():
    order_list = orders.Order.objects()
    #orders = db_getters.get_orders()
    return render_template('bartender/current_orders.html', title='Orders', user=current_user,
                           orders=order_list)

#TODO do not need?
@bartender.route("/order_complete", methods=["POST"])
@login_required
@bartender_required
def order_complete():
    print(current_user.username)
    data = request.json
    print(data)
    if(set(data.keys()) == set(["_id"])):
        print("we here")
        #the_order = db_getters.get_order(data['_id'])
        the_order = orders.Order.get(id=ObjectId(data['_id']))
        db.PastOrders.insert_one(the_order)
        print(the_order)
        if(the_order is not None):
            the_order.complete_order()
    #orders = db_getters.get_orders()
    order_list = orders.Order.objects()
    return render_template('bartender/current_orders.html', title='Orders', user=current_user,
                           orders=orders)
