"""
Problem Statement:
You are working on building a file sharing system to share a very large file which consists of m small chunks with IDs from 1 to m.
When users join the system, the system should assign a unique ID to them. 
The unique ID should be used once for each user, but when a user leaves the system, the ID can be reused again. The unique ID starts from 1.
Users can request a certain chunk of the file, the system should return a list of IDs of all the users who own this chunk. 
If the user receives a non-empty list of IDs, they receive the requested chunk successfully.
"""

class FileSharingSystem:
    def __init__(self, m):
        self.chunkToUsersMap = {}
        self.availableIDsMinHeap = []
        self.nextIDToBeGenerated = 1
        self.userToChunkIdMap = {}
        for i in range(1, m + 1):
            users = set()
            self.chunkToUsersMap[i] = users

    def join(self, ownedChunks):
        assignedId = 1  # id starts from 1
        if self.availableIDsMinHeap:
            assignedId = self.availableIDsMinHeap.pop(0)
        else:
            assignedId = self.nextIDToBeGenerated
            self.nextIDToBeGenerated += 1
    
        for chunkId in ownedChunks:
            chunkOwners = self.chunkToUsersMap[chunkId]
            chunkOwners.add(assignedId)
        self.userToChunkIdMap[assignedId] = set(ownedChunks)
        return assignedId

    def leave(self, userId):
        if userId in self.userToChunkIdMap:
            for chunkID in self.userToChunkIdMap[userId]:
                self.chunkToUsersMap[chunkID].discard(userId)
            del self.userToChunkIdMap[userId]
            self.availableIDsMinHeap.append(userId)

    def request(self, userId, chunkId):
        if chunkId not in self.chunkToUsersMap:
            return []
        chunkOwners = list(self.chunkToUsersMap[chunkId])
        if userId not in self.userToChunkIdMap:
            self.chunkToUsersMap[chunkId].add(userId)
            self.userToChunkIdMap[userId] = set([chunkId])
        elif userId not in chunkOwners:
            self.chunkToUsersMap[chunkId].add(userId)
            self.userToChunkIdMap[userId].add(chunkId)
        return chunkOwners

fileSharing = FileSharingSystem(4)
print(fileSharing.join([1, 2]))   # Output: 1
print(fileSharing.join([2, 3]))   # Output: 2
print(fileSharing.join([4]))      # Output: 3
print(fileSharing.request(1, 3))  # Output: [2]
print(fileSharing.request(2, 2))  # Output: [1, 2]
fileSharing.leave(1)
print(fileSharing.request(2, 1))  # Output: []
fileSharing.leave(2)
print(fileSharing.join([]))       # Output: 1


"""
FileSharingSystem fileSharing = new FileSharingSystem(4); // We use the system to share a file of 4 chunks.

fileSharing.join([1, 2]);    // A user who has chunks [1,2] joined the system, assign id = 1 to them and return 1.

fileSharing.join([2, 3]);    // A user who has chunks [2,3] joined the system, assign id = 2 to them and return 2.

fileSharing.join([4]);       // A user who has chunk [4] joined the system, assign id = 3 to them and return 3.

fileSharing.request(1, 3);   // The user with id = 1 requested the third file chunk, as only the user with id = 2 has the file, return [2] . Notice that user 1 now has chunks [1,2,3].

fileSharing.request(2, 2);   // The user with id = 2 requested the second file chunk, users with ids [1,2] have this chunk, thus we return [1,2].

fileSharing.leave(1);        // The user with id = 1 left the system, all the file chunks with them are no longer available for other users.

fileSharing.request(2, 1);   // The user with id = 2 requested the first file chunk, no one in the system has this chunk, we return empty list [].

fileSharing.leave(2);        // The user with id = 2 left the system.

fileSharing.join([]);        // A user who doesn't have any chunks joined the system, assign id = 1 to them and return 1. Notice that ids 1 and 2 are free and we can reuse them.
 
"""