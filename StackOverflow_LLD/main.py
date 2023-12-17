# Import necessary classes
from stackOverflow.Status import Status
from stackOverflow.TextPhotoBasedEntity import TextPhotoBasedEntity
from stackOverflow.Question import Question
from stackOverflow.Answer import Answer
from stackOverflow.Comment import Comment
from stackOverflow.Photo import Photo
from stackOverflow.Bounty import Bounty
from stackOverflow.Tag import Tag
from stackOverflow.Member import Member, AccountStatus

# Instantiate a Member
member1 = Member(id=1)
member1._name = "John Doe"
member1._displayName = "John"
member1._email = "john.doe@example.com"

# Instantiate a Question
question1 = Question(id=1, askingMember=member1, title="How to use Python?", text="I am new to Python, and I want to learn how to use it.", photos=[], tags=["python"], bounty=None)

# Instantiate an Answer
answer1 = Answer(id=1, creatingMember=member1, text="You can start by installing Python and then exploring online tutorials.", photos=[])

# Instantiate a Comment
comment1 = Comment(id=1, commenter=member1, text="Great answer!",photos=[])

# Instantiate a Photo
photo1 = Photo(id=1, photoPath="/path/to/photo.jpg", creator=member1)

# Instantiate a Bounty
bounty1 = Bounty(reputation=50, expirationDate="2023-12-31")

# Instantiate a Tag
tag1 = Tag(text="python")

# Perform actions
question1.addAnswer(answer1)
question1.addComment(comment1)
question1.addPhotos([photo1])
question1.receiveBounty(50, creator=member1)
question1.close()

# Display information
print(f"Question Title: {question1.getTitle()}")
print(f"Question Status: {question1.getStatus()}")
print(f"Question Tags: {question1.getTags()}")
print(f"Question Answers: {question1.getAnswers()}")
print(f"Question Comments: {question1.getComments()}")
print(f"Question Photos: {question1.getPhotos()}")
print(f"Question Bounty: {question1.getBounty()}")

print(f"Answer Text: {answer1.getText()}")
print(f"Answer Status: {answer1.getStatus()}")
print(f"Answer Comments: {answer1.getComments()}")

print(f"Comment Text: {comment1.getText()}")
print(f"Comment Status: {comment1.getStatus()}")

print(f"Photo Path: {photo1.getPhotoPath()}")
print(f"Photo Creation Date: {photo1.getCreationDate()}")
print(f"Photo Creating Member: {photo1.getCreatingMember()}")

print(f"Bounty Reputation: {bounty1._reputation}")
print(f"Bounty Expiration Date: {bounty1._expirationdate}")

print(f"Tag Text: {tag1.getText()}")

print(f"Member Reputation: {member1.getReputation()}")
print(f"Member Status: {member1.getStatus()}")
print(f"Member Name: {member1.getName()}")
print(f"Member Display Name: {member1.getDisplayName()}")
print(f"Member Email: {member1.getEmail()}")
