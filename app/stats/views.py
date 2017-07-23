from flask import render_template, redirect, request, url_for
from . import admin
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
def credit_management():
    users = db.Users.find()
    return render_template("admin/credits.html", users=users)

@admin.route("/add_credits/<username>", methods=["POST", "GET"])
@login_required
@admin_required
def add_user_credits(username):
    form = AddCreditsForm()
    if(request.method == "POST" and form.validate_on_submit()):
        return redirect('index')
        #TODO
    else:
        user = db.Users.find({"username" : username})
        if user is not None:
            return render_remplate('admin/add_credits.html', title='Add Credits', user=username)
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
    shutdown_server()
    return "Party ended"

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
