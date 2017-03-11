from flask import render_template, redirect, request, url_for
from . import admin
from pymongo import MongoClient
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, login_required
from ..objects import User
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

@admin.route("/credits")
@login_required
@admin_required
def credit_management():
    users = db.Users.find()
    return render_template("admin/credits.html", users=users)

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
