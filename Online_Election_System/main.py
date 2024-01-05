from onlineElectionSystem import OnlineElectionSystem
# Create an instance of OnlineElectionSystem
election_system = OnlineElectionSystem()

# Process votes
election_system.processVote(1, "CandidateA")
election_system.processVote(2, "CandidateB")
election_system.processVote(3, "CandidateA")
election_system.processVote(4, "CandidateB")
election_system.processVote(5, "CandidateA")

# Get the leading person at different times
print("Leading person at time 1:",election_system.getPersonLeading(1))  # Output: CandidateA
print("Leading person at time 3:",election_system.getPersonLeading(3))  # Output: CandidateA
print("Leading person at time 4:",election_system.getPersonLeading(4))  # Output: CandidateB (in the case of a tie, the most recent vote (among tied candidates) wins.)
print("Leading person at time 5:",election_system.getPersonLeading(5))  # Output: CandidateA
print("Leading person at time 6:",election_system.getPersonLeading(6))  # Output: CandidateA (since no more votes)
