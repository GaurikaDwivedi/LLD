class RoomHouseKeeping:
    all_entries = []
    def __init__(self, room, date, status):
        self.room = room
        self.date = date
        self.status = status
        RoomHouseKeeping.all_entries.append(self)

    def get_room(self):
        return self.room

    def get_date(self):
        return self.date

    def get_status(self):
        return self.status


    @classmethod
    def display_all_entries(cls):
        print("All Room Housekeeping Entries:")
        for entry in cls.all_entries:
            print("Room Number:", entry.get_room().get_room_number())
            print("Room Style:", entry.get_room().get_room_style())
            print("Date:", entry.get_date())
            print("Status:", entry.get_status())
            print()