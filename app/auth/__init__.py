from flask import Blueprint

#create a blueprint object and initialize it with a name
auth = Blueprint('auth', __name__)

from . import views