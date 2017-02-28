from flask import render_template, redirect, request, url_for
from . import admin
from .forms import LoginForm
from pymongo import MongoClient
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user
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
@admin_required
def admin():
    logout_user()
    return redirect('index')
