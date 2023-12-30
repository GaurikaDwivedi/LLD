class Notification:
    def __init__(self, message, recipient):
        self.message = message
        self.recipient = recipient

    def get_message(self):
        return self.message

    def get_recipient(self):
        return self.recipient
