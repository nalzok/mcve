from app.stuff.models import Stuff


def update_stuff(stuff):
    stuff.state = Stuff.next_state(stuff.state)
