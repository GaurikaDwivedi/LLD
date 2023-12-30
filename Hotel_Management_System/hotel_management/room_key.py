class RoomKey:
    def __init__(self, room, key_id, barcode):
        self.room = room
        self.key_id = key_id
        self.barcode = barcode

    def get_room(self):
        return self.room

    def get_key_id(self):
        return self.key_id

    def get_barcode(self):
        return self.barcode
