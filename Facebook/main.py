from facebook.member import Member
from facebook.post import Post
from facebook.group import Group
from facebook.page import Page
from facebook.message import Message
from facebook.friendRequest import FriendRequest
from facebook.address import Address

user1 = Member()
user1.setName("John Doe")
user1.setEmail("john@example.com")
address1 = Address(streetAddress="123 Main St", city="City1", state="State1", zipCode="12345", country="Country1")
user1.setAddress(address1)

# Accessing attributes
user2 = Member()
user2.setName("Chris")
user2.setEmail("jane@example.com")
address2 = Address(streetAddress="456 Side St", city="City2", state="State2", zipCode="67890", country="Country2")

user3 = Member()
user3.setName("Sally Doe")
user3.setEmail("sally@example.com")
address3 = Address(streetAddress="876 Side St", city="City3", state="State3", zipCode="67590", country="Country3")

user4 = Member()
user4.setName("John Kraus")
user4.setEmail("kraus@example.com")
address4 = Address(streetAddress="098 Side St", city="City4", state="State4", zipCode="57890", country="Country4")

post1 = Post(contentId=1, text="Hello, World!", blobUrlsForPhotos=["photo1.jpg"], creator=user1)
post2 = Post(contentId=2, text="Bye, World!", blobUrlsForPhotos=["photo2.jpg"], creator=user2)

group1 = Group(groupId=1, name="Tech Enthusiasts", description="A group for tech discussions", creator=user1)
group1.addModerator(user4)
page1 = Page(pageId=1, name="Tech News", description="Latest technology updates", creator=user1)
user3.followPage(page1)
user4.followPage(page1)
message1 = Message(messageId=1, messageBody="Hi, how are you?", creator=user1)
message1.addMember(user2)

friend_request1 = FriendRequest(requestSender=user1, memberInvited=user2)
user2.setFriendRequestsReceived(user1)
user1.setFriendRequestsSent(user2)

friend_request2 = FriendRequest(requestSender=user3, memberInvited=user2)
user2.setFriendRequestsReceived(user3)
user3.setFriendRequestsSent(user2)

user1_sent_req = user1.getFriendRequestsSent()
print(f"{user1.getName()}'s friend requests sent to: {[member.getName() for member in user1_sent_req]} ")

user2_received_req =  user2.getFriendRequestsReceived()
print(f"{user2.getName()}'s friend requests received from: {[member.getName() for member in user2_received_req]}")

user3_sent_req = user1.getFriendRequestsSent()
print(f"{user3.getName()}'s friend requests sent to: {[member.getName() for member in user3_sent_req]} ")

user2_received_req =  user2.getFriendRequestsReceived()
print(f"{user2.getName()}'s friend requests received from: {[member.getName() for member in user2_received_req]}")

# Accept or reject friend request
friend_request1.accept() 
friend_request2.reject()  

user1_sent_req_after = user1.getFriendRequestsSent()
print(f"{user1.getName()}'s sent friend requests list: {[member.getName() for member in user1_sent_req_after]} ")

user2_received_req_after =  user2.getFriendRequestsReceived()
print(f"{user2.getName()}'s received friend requests list: {[member.getName() for member in user2_received_req_after]}")

# Demonstrate some functionalities
user1.addNewPost(post1)
group1.addPost(post1)
user2.addGroupPost(post2, group1)

user1.joinGroup(group1)
user2.joinGroup(group1)

user1.followPage(page1)

user1.sendMessage(message1)
user2.sendMessage(message1)

# Print some information
posts = user1.getAllPosts()
print(f"{user1.getName()}'s posts:")
for post in posts:
    print(f"Id: {post.getContentId()}. Text: {post.getText()}, Likes: {post.getTotalLikes()}, CreationDateTime: {post.getCreationDateTime()}")

user1_groups = user1.getGroups()
print(f"{user1.getName()}'s groups:")
for group in user1_groups:
    print(f"Id: {group.getGroupId()}. Name: {group.getName()}, Description: {group.getDescription()}, Members: {[member.getName() for member in group.getMembers()]}, Moderator: {[member.getName() for member in group.getModerators()]}, Posts in Group: {[post.getContentId() for post in group.getPosts()]}")

user1_followed_pages = user1.getPageFollowed()
print(f"{user1.getName()}'s Followed below Pages:")
for page in user1_followed_pages:
    print(f"Id: {page.getPageId()}. PageName: {page.getPageName()}, Description: {page.getDescription()}, Other Followers of Page: {[follower.getName() for follower in page.getFollowers()]}")

user4.unfollowPage(page1)
# Update profile information
user1.setProfilePictureBlobUrl("profile_picture.jpg")
user1.setCoverPhotoBlobUrl("cover_photo.jpg")

# Display user information
print(f"{user1.getName()}'s profile picture:", user1.getProfilePictureBlobUrl())
print(f"{user1.getName()}'s cover photo:", user1.getCoverPhotoBlobUrl())