class Notification:
    def __init__(self, message):
        self._message = message

    def schedule(self):
        pass

    def send(self):
        print(f"Notification: {self.getMessage()}")

    def getMessage(self):
        return self._message

    def setMessage(self, message):
        self._message = message