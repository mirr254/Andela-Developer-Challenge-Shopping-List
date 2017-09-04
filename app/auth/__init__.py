from flask import Blueprint

#create a blueprint object and initialize it with a name
auth1 = Blueprint('auth', __name__)

from . import views