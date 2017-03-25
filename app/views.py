from flask import render_template, flash, redirect, request, url_for
from app import app
from pymongo import MongoClient
from bson.objectid import ObjectId
from werkzeug.security import check_password_hash
from flask_login import login_required, login_user, logout_user, current_user
from .objects import User
from .decorators import bartender_required, admin_required
from .db import db
import json
import time

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
@app.route("/")
@app.route("/index")
def index():
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
    return render_template('index.html', title='Home', user=current_user, drinks=drinks)

# list_drinks
#   lists all drink recipes in the database
#
# returns
#   drinks template with all recorded drinks
@app.route("/list_drinks", methods=["GET", "POST"])
@app.route("/recipes", methods=["GET", "POST"])
def list_drinks():
    return render_template('recipes.html', title='All Drinks', user=current_user, drinks=db.Drinks.find())

# menu
#   lists all available drinks based on alchohol currently in stock
#
# returns
#   menu template with only available drinks

@app.route("/menu", methods=["GET"])
def menu():
    if(current_user.is_authenticated):
        return render_template('menu_auth.html', title='Menu',
                           user=current_user,
                           credits=get_user_credits(current_user.username),
                           drinks=db.Drinks.find({"available": True}))
    else:
         return render_template('menu_unauth.html', title='Menu',
                           drinks=db.Drinks.find({"available": True}))

@app.route("/recent_orders")
@login_required
def recent_orders():
    orders = db.Orders.find({"user": current_user.username})
    return render_template('recent_orders.html',
                           title='Orders',
                           user=current_user,
                           orders=orders,
                           totaldrinks=get_user_drinks(current_user.username),
                           credits=get_user_credits(current_user.username))

@app.route('/review_order/<drinkname>')
@login_required
def review_order(drinkname):
    drink = db.Drinks.find_one({"name": drinkname})
    if drink is not None:
        return render_template('review_order.html', title='Review and Order', user=current_user, drink=drink)
    else:
        return redirect(url_for('menu'))

#Need to test order_drink statistics more, but is backed up in completed orders anyways
@app.route('/order_drink', methods=["POST"])
@login_required
def order_drink():
    postData = dict(request.form)
    drink = db.Drinks.find_one({"name": postData['drink'][0]})
    if drink is not None:
        if get_user_credits(current_user.username) < drink['cost']:
            return '{"status": "failed - not enough credits"}'
        print("drink ordered since enough credits")
        db.Users.update_one({'username': current_user.username},
                            {
                            '$inc': {
                                    'credits': -drink['cost'],
                                    'drinksOrdered': 1
                                }
                            })
        print("credits edited")
        db.Orders.insert_one(
             {
                 "name": drink['name'],
                 "cost": drink['cost'],
                 "type": drink['type'],
                 "recipe": drink['recipe'],
                 "image": drink['image'],
                 "timeOrdered": int(time.time()),
                 "user": current_user.username,
                 "instructions": postData['instructions'][0],
                 "status": "queued"
             }
        )
        print("trying statistics")
        try:
            global CURRENT_STAT_FILE
            stats = db.Statistics.find_one({"id": CURRENT_STAT_FILE})
            if stats is not None:
                # loop through stats see until not exist or less than current stat file time
                if (int(time.time()*1000) - stats['time']) >= 3600:
                    print("test!!!")
                    #An hour or more has passed
                    CURRENT_STAT_FILE = CURRENT_STAT_FILE + 1
                    statistics.insert_one(
                        {
                            "id": CURRENT_STAT_FILE,
                            "time": int(time.time()*1000) ,
                            "total_orders": 1,
                            "drink_orders": [
                                {"name": drink['name'], "Orders": 1},
                            ]
                        })
                else:
                    #Wait what the hell is happening, how do I incriment a drinks Orders
                    stat_exists = db.Statistics.find_one({"name" : drink['name']})
                    if stat_exists:
                        db.Users.update_one({'id': CURRENT_STAT_FILE},
                                            {
                                            '$inc': {
                                                    'total_orders': 1
                                                }
                                            })
                    else:
                        db.Users.update_one({'id': CURRENT_STAT_FILE},
                                        {
                                        '$inc': {
                                                'total_orders': 1
                                            },
                                        '$addToSet': {
                                                'name' : drink['name'], 'Orders': 1
                                            }

                                        })
            else:
                db.Statistics.insert_one(
                        {
                            "id": CURRENT_STAT_FILE,
                            "time": int(time.time()*1000),
                            "total_orders": 1,
                            "drink_orders": [
                                {"name": drink["name"], "Orders": 1},
                            ]
                        })

        except Exception as e:
            print(e)
        return '{"status": "okay"}'
    else:
        return '{"status": "failed - no such drink"}'

@app.route('/cancel_drink', methods=["POST"])
@login_required
def cancel_drink():
    postData = dict(request.form)
    orderid = ObjectId(postData['order'][0])
    order = db.Orders.find_one({"_id": orderid})
    if order is not None:
        if order['status'].lower() == "queued":
            db.Orders.delete_one({"_id": orderid, "user": current_user.username})
            db.Users.update_one({'username': current_user.username},
                    {
                    '$inc': {
                            'credits': order['cost'],
                            'drinksOrdered': -1
                        }
                    })

            return '{"status": "okay"}'
        return '{"status": "cannot cancel progressed order"}'
    else:
        return '{"status": "failed - no such order"}'

@app.route('/custom_drink')
@login_required
def custom_drink():
    ingredients = db.Ingredients.find({"available": True})
    return render_template('custom_drink.html', ingredients=ingredients)

@app.route('/order_custom_drink', methods=["POST"])
@login_required
def order_custom_drink():
    recipe = []
    postData = dict(request.form)
    print(postData['recipe[]'])
    if get_user_credits(current_user.username) < CUSTOM_COST:
        print ("Can't afford drink")
        return '{"status": "failed - not enough credits"}'

    for ing in postData['recipe[]']:
        print(ing)

        ingredient = {}
        ingredient['type'] = ing
        ingredient['flavor'] = ''
        ingredient['amount'] = ""
        recipe.append(ingredient)

    db.Users.update_one({'username': current_user.username},
                        {
                        '$inc': {
                                'credits': -CUSTOM_COST,
                                'drinksOrdered': 1
                            }
                        })
    db.Orders.insert_one(
         {
             "name": "Custom Drink",
             "cost": CUSTOM_COST,
             "type": "custom",
             "recipe": recipe,
             "image": 'custom_drink.png',
             "timeOrdered": int(time.time()),
             "user": current_user.username,
             "instructions": postData['instructions'][0],
             "status": "queued"
         }
    )
    return '{"status": "okay"}'


@app.route("/order_complete", methods=["POST"])
@login_required
@bartender_required
def order_complete():
    print(current_user.username)
    data = request.json
    print(data)
    if(set(data.keys()) == set(["_id"])):
        print("we here")
        the_order = db.Orders.find_one({"_id": ObjectId(data["_id"])})
        db.PastOrders.insert_one(the_order)
        print(the_order)
        if(the_order is not None):
            db.Orders.delete_one({"_id": ObjectId(data["_id"])})
    orders = db.Orders.find()
    return render_template('current_orders.html', title='Orders', user=current_user, orders=orders)

def get_user_credits(username):
    usr = db.Users.find_one({'username': username})
    return usr['credits']
def get_user_drinks(username):
    usr = db.Users.find_one({'username': username})
    return usr['drinksOrdered']
