from app.stuff.models import Stuff
from app.business_logic import update_stuff


def populate_db():
    for _ in range(5):
        stuff = Stuff()
        update_stuff(stuff)
        stuff.save()
