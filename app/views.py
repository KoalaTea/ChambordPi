from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from pymongo import MongoClient

client = MongoClient()
db = client.ChambordPi
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
    if(form.validate_on_submit()):
        flash('Login for username="%s" and password="%s"' % (form.username.data, form.password.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route("/list_alchohal", methods=["GET", "POST"])
def list_alchohal():
    pass

@app.route("/list_drinks", methods=["GET", "POST"])
def list_drinks():
    for drink in db.Drinks.find():
        print(drink)
    return render_template('drinks.html', title='All Drinks', user=user, drinks=db.Drinks.find())

@app.route("/menu", methods=["GET", "POST"])
def menu():
    pass

@app.route("/orders", methods=["GET", "POST"])
def orders():
    pass
