class Invoice:
    def __init__(self, room, charges):
        self.room = room
        self.charges = charges

    def get_room(self):
        return self.room

    def get_charges(self):
        return self.charges
