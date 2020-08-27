from app.business_logic import update_stuff
from . import stuff
from .models import Stuff


@stuff.route('/')
def index():
    # Pretend s is loaded from some database...
    s = Stuff()
    update_stuff(s)
    return f''
