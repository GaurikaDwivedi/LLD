import time
from enum import Enum

class FriendRequestStatus(Enum):
    PENDING = 0
    ACCEPTED = 1
    REJECTED = 2
    CANCELED = 3


class FriendRequest:
    def __init__(self, requestSender, memberInvited):
        self._dateRejectedOrAccepted = 0

        self._requestSender = requestSender
        self._memberInvited = memberInvited
        self._status = FriendRequestStatus.PENDING
        self._dateCreated = round(time.time() * 1000)

    def accept(self):
        if self._status != FriendRequestStatus.CANCELED and self._status != FriendRequestStatus.REJECTED:
            self._status = FriendRequestStatus.ACCEPTED
            print(f"{self.getMemberInvited().getName()} Accepted Request from {self.getRequestSender().getName()}!!")
            self._dateRejectedOrAccepted = round(time.time() * 1000)
            self._requestSender.getFriendRequestsSent().remove(self._memberInvited)
            self._memberInvited.getFriendRequestsReceived().remove(self._requestSender)
            return True
        return False

    def reject(self):
        if self._status != FriendRequestStatus.CANCELED and self._status != FriendRequestStatus.ACCEPTED:
            self._status = FriendRequestStatus.REJECTED
            print(f"{self.getMemberInvited().getName()} Rejected Request from {self.getRequestSender().getName()}!!")
            self._dateRejectedOrAccepted = round(time.time() * 1000)
            self._requestSender.getFriendRequestsSent().remove(self._memberInvited)
            self._memberInvited.getFriendRequestsReceived().remove(self._requestSender)
            return True
        return False

    def getRequestSender(self):
        return self._requestSender

    def getMemberInvited(self):
        return self._memberInvited

    def getStatus(self):
        return self._status

    def getDateCreated(self):
        return self._dateCreated

    def getDateRejectedOrAccepted(self):
        return self._dateRejectedOrAccepted

    def send(self):
        self._requestSender.getFriendRequestsSent().add(self)
        self._memberInvited.getFriendRequestsReceived().add(self)

    def __eq__(self, other):
        if isinstance(other, FriendRequest):
            return (
                self._requestSender == other._requestSender
                and self._memberInvited == other._memberInvited
                and self._status == other._status
            )
        return False

    def __hash__(self):
        return hash((self._requestSender, self._memberInvited, self._status))



    