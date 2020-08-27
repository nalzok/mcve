class Stuff:
    def __init__(self):
        self.state = 0

    def save(self):
        print(f'Pretend we are saving {self} to some database...')

    @staticmethod
    def next_state(state):
        return state + 1
