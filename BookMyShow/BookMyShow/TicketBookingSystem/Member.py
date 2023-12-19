class Member:
    def __init__(self, id, name, email, phone):
        self._id = id
        self._name = name
        self._email = email
        self._phone = phone

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getEmail(self):
        return self._email

    def setEmail(self, email):
        self._email = email

    def getPhone(self):
        return self._phone

    def setPhone(self, phone):
        self._phone = phone

    def getId(self):
        return self._id

    def equals(self, o):
        if self is o:
            return True
        if o is None or type(o) != Member:
            return False
        member = o
        return self._id == member._id

    def hashCode(self):
        return hash(self._id)
