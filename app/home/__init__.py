from flask import Blueprint

#create a blueprint object and initialize it with a name
home = Blueprint('home', __name__)

from . import views