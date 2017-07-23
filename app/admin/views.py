from flask import render_template, redirect, request, url_for
from . import admin
from .forms import AddCreditsForm
from pymongo import MongoClient
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, login_required
from ..objects.users import User
from ..db import db
from ..decorators import admin_required


# logout
#   logour page destroys session
#
# data
#   login information
#
# returns
#   cleared session and redirect to index
@admin.route("/admin")
@login_required
@admin_required
def admin_page():
    logout_user()
    return redirect('index')

@admin.route("/manage_credits")
@login_required
@admin_required
def manage_credits():
    form = AddCreditsForm()
    users = db.Users.find()
    return render_template("admin/credits.html", users=users, form=form, cred_default=500)

@admin.route("/add_credits/<username>", methods=["POST", "GET"])
@login_required
@admin_required
def add_credits(username):
    form = AddCreditsForm()
    if((request.method == "POST" and all(x in request.form for x in ['username', 'credits'])) or form.validate_on_submit()):
        username = request.form['username']
        credits = request.form['credits']
        #TODO check for negatives
        if credits.isdigit():
            add_user_credits(username, credits)

        return redirect(url_for('admin.manage_credits'))
    else:
        user = db.Users.find({"username" : username})
        if user is not None:
            return render_template('admin/add_credits.html', title='Add Credits', user=username, form=form)
        else:
            return redirect('manage_credits')

@admin.route("/end_party")
@login_required
@admin_required
def end_party():
    users = db.Users.find()
    for user in users:
        if 'admin' not in user['roles']:
            db.Users.update_one({'username': user['username']},
                    {
                    '$set': {
                            'credits': 0
                            }
                    })
    shutdown_server() #TODO behind nginx how does this work?
    return "Party ended"

def add_user_credits(username, credits):
    user = db.User.find({'username': username})
    if user is not None:
        db.Users.update_one({'username': username},
                {
                '$inc': {
                    'credits': int(credits)
                    }
                })

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
