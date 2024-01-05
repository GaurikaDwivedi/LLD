class OnlineElectionSystem:
    def __init__(self):
        self.personLeading = {} # entry [i, j] implies person j is the person leading in the election at time i
        self.votesAcquired = {} # entry [i, k] implies person i has gotten k votes yet
        self.timesVotesHaveBeenCast = [] # data structure to keep all the times at which a vote has been cast
        self.personLeadingSoFar = -1 # person leading till now

    def processVote(self, time, votedPerson):
        self.timesVotesHaveBeenCast.append(time)
        value = 0
        if votedPerson in self.votesAcquired:
            value = self.votesAcquired[votedPerson]
        self.votesAcquired[votedPerson] = value + 1
        value = 0
        if votedPerson in self.votesAcquired:
            if self.personLeadingSoFar in self.votesAcquired:
                value = self.votesAcquired[self.personLeadingSoFar]
        if self.personLeadingSoFar != votedPerson and self.votesAcquired[votedPerson] >= value:
            self.personLeadingSoFar = votedPerson  # remember in the case of a tie, the most recent vote (among tied candidates) wins.
        self.personLeading[time] = self.personLeadingSoFar

    def getPersonLeading(self, t):
        return self.personLeading[self._getTimeEqualToOrLessThan(t)]

    def _getTimeEqualToOrLessThan(self, time):
        """
        binary search:
        search the minimum value from search space
        that is greater or equal to than the input time. Let's say index of this value is i;
        That way our answer would be timesVotesHaveBeenCast[i - 1] if timesVotesHaveBeenCast[i] > input time
        otherwise timesVotesHaveBeenCast[i]
        """
        left = 0
        right = len(self.timesVotesHaveBeenCast) - 1
        while left < right:
            mid = left + ((right - left) // 2)
            if self.timesVotesHaveBeenCast[mid] >= time:
                right = mid
            else:
                left = mid + 1
        return self.timesVotesHaveBeenCast[left] if self.timesVotesHaveBeenCast[left] <= time else self.timesVotesHaveBeenCast[left - 1]