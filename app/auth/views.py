from flask import render_template, redirect, request, url_for
from . import auth
from app.auth.forms import LoginForm, SignUpForm
from pymongo import MongoClient
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user
from app.objects.users import User
from app.objects import users

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
    if(request.method == "POST"):
        if form.validate_on_submit():
            try:
                user = users.User.objects.get(username=form.username.data)
                if user.validate_login(user.password, form.password.data):
                    login_user(user)
                    return redirect(url_for('views.index'))
            except:
                pass
        return render_template('auth/login.html', title='Sign In', form=form, message='Login Failed')
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
    return redirect(url_for('views.index'))

@auth.route("/signup", methods=["POST", "GET"])
def signup():
    form = SignUpForm()
    if(form.validate_on_submit()):
        user = users.User.objects.get({form.username.data})
        if(user is None and (form.password.data == form.repassword.data)):
            users.create_user(form.username.data, form.password.data)
        else:
            return redirect(url_for('auth.signup'))
        return redirect('auth.login')
    return render_template('auth/signup.html', title='Sign Up', form=form)
