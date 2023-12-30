class Hotel:
    def __init__(self, name):
        self.locations = []
        self.name = name

    def add_location(self, location):
        self.locations.append(location)

    def get_name(self):
        return self.name

    def get_locations(self):
        return self.locations