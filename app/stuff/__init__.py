from flask import Blueprint

stuff = Blueprint('stuff', __name__, template_folder='templates')

from . import views
