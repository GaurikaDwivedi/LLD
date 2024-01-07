from enum import Enum

class Member:

    def __init__(self):
        self._userId = None
        self._name = None
        self._address = None
        self._email = None
        self._phone = None
        self._memberSince = None
        self._messages = set()
        self._friendsList = set()
        self._friendRequestsSent = set()
        self._friendRequestsReceived = set()
        self._pagesFollowed = set()
        self._groups = set()
        self._posts = set()
        self._profilePictureBlobUrl = None
        self._coverPhotoBlobUrl = None
        self._gender = None
        self._workExperiences = set()
        self._educations = set()
        self._placesCheckedIn = set()

    class AccountStatus(Enum):
        ACTIVE = 0
        DELETED = 1
        BLACKLISTED = 2
        DEACTIVATED = 3

    def addWorkExperience(self, work):
        self._workExperiences.add(work)

    def addEducation(self, education):
        self._educations.add(education)

    def checkInPlace(self, place):
        self._placesCheckedIn.add(place)

    def sendMessage(self, message):
        message.send()

    def getAllPosts(self):
        return self._posts

    def addNewPost(self, post):
        self._posts.add(post)

    def addPagePost(self, post, page):
        if page.getCreator() is self:
            page.getPosts().add(post)
            return True
        return False

    def addGroupPost(self, post, group):
        if self in group.getMembers():
            group.getPosts().add(post)
            return True
        else:
            print(f"{self.getName()} is not group member, hence can't post.")
        return False

    def sendFriendRequest(self, friendRequest):
        friendRequest.send()

    def acceptFriendRequest(self, friendRequest):
        friendRequest.accept()

    def rejectFriendRequest(self, friendRequest):
        friendRequest.reject()

    def blockUser(self, member, group):
        if self in  group.getAdmins():
            group.getMembers().remove(member)

    def unblockUser(self, member, group):
        if self in group.getAdmins() and member in group.getBannedmembers():
            group.getBannedmembers().remove(member)
            group.getMembers().add(member)

    def createPage(self, page):
        self._pagesFollowed.add(page)

    def getUserId(self):
        return self._userId

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getAddress(self):
        return self._address

    def setAddress(self, address):
        self._address = address

    def getEmail(self):
        return self._email

    def setEmail(self, email):
        self.email = email

    def getPhone(self):
        return self._phone

    def setPhone(self, phone):
        self.phone = phone

    def getMemberSince(self):
        return self._memberSince

    def getMessages(self):
        return self._messages

    def getFriendsList(self):
        return self._friendsList
    
    def setFriendRequestsSent(self, member):
        return self._friendRequestsSent.add(member)
    
    def getFriendRequestsSent(self):
        return self._friendRequestsSent
    
    def setFriendRequestsReceived(self, member):
        return self._friendRequestsReceived.add(member)
    
    def getFriendRequestsReceived(self):
        return self._friendRequestsReceived

    def getGroups(self):
        return self._groups

    def joinGroup(self, group):
        self._groups.add(group)
        group.getMembers().add(self)

    def leaveGroup(self, group):
        if group in self._groups:
            self._groups.add(group)
            group.getMembers().add(self)
            return True
        return False

    def followPage(self, page):
        self._pagesFollowed.add(page)
        page.getFollowers().add(self)

    def unfollowPage(self, page):
        if page in self._pagesFollowed:
            self._pagesFollowed.remove(page)
            page.getFollowers().remove(self)
            print(f"{self.getName()} unfollowed page- {page.getPageName()}")
            return True
        return False

    def getPageFollowed(self):
        return self._pagesFollowed
    
    def getProfilePictureBlobUrl(self):
        return self._profilePictureBlobUrl

    def setProfilePictureBlobUrl(self, profilePictureBlobUrl):
        self._profilePictureBlobUrl = profilePictureBlobUrl

    def getCoverPhotoBlobUrl(self):
        return self._coverPhotoBlobUrl

    def setCoverPhotoBlobUrl(self, coverPhotoBlobUrl):
        self._coverPhotoBlobUrl = coverPhotoBlobUrl

    def getGender(self):
        return self._gender

    def setGender(self, gender):
        self.gender = gender

    def getWorkExperiences(self):
        return self._workExperiences

    def getEducations(self):
        return self._educations

    def getCheckedInPlaces(self):
        return self._placesCheckedIn

    def equals(self, o):
        if self is o:
            return True
        if o is None or type(o) != Member:
            return False
        member = o
        return self._userId is member.userId

    def hashCode(self):
        return hash(self._userId)