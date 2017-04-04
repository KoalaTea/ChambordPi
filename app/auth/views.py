from flask import render_template, redirect, request, url_for
from . import auth
from .forms import LoginForm, SignUpForm
from pymongo import MongoClient
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user
from ..objects import User
from ..db import db

# TODO:
#   set all pages to check for authentication and if none - guest@Hackerbar
#   metrics
#   logging

# login
#   login page
#
# data
#   username    - the username
#   password    - the password
#
# returns
#   login stuff if successful and redirect to index or flashed failed message if unsuccessful
@auth.route("/login", methods=["POST", "GET"])
@auth.route("/signin", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if(request.method == "POST" and form.validate_on_submit()):
        user = db.Users.find_one({"username": form.username.data})
        if(user is not None and User.validate_login(user['password'], form.password.data)):
            user_obj = User(user)
            login_user(user_obj)
        else:
            return render_template('auth/login.html', title='Sign In', form=form, message='Login Failed')
            #TODO
        return redirect(url_for('index'))
    return render_template('auth/login.html', title='Sign In', form=form, message=None)

# logout
#   logour page destroys session
#
# data
#   login information
#
# returns
#   cleared session and redirect to index
@auth.route("/logout")
@auth.route("/signout")
def logout():
    logout_user()
    return redirect('index')

@auth.route("/signup", methods=["POST", "GET"])
def signup():
    form = SignUpForm()
    if(form.validate_on_submit()):
        user = db.Users.find_one({"username": form.username.data})
        if(user is None and (form.password.data == form.repassword.data)):
            db.Users.insert_one({"username":form.username.data, "password":generate_password_hash(form.password.data), "credits":0, "roles":["user"], "drinksOrdered":0})
        else:
            return redirect(url_for('auth.signup'))
        return redirect('index')
    return render_template('auth/signup.html', title='Sign Up', form=form)
