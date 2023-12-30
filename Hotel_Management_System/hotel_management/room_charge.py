class RoomCharge:
    def __init__(self, room, charge_name, charge_amount):
        self.room = room
        self.charge_name = charge_name
        self.charge_amount = charge_amount

    def get_room(self):
        return self.room

    def get_charge_name(self):
        return self.charge_name

    def get_charge_amount(self):
        return self.charge_amount
