from flask import Blueprint

bartender = Blueprint('bartender', __name__)

from . import views
