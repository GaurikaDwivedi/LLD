class AuthenticationManager:
    def __init__(self, timeToLive):

        self.ttl = timeToLive
        self.tokenToTimeMap = {} # maps unexpired tokens to their expiration time
        self.timeToTokenMap = {} # maps time to tokens generated at a given time.
        # times, which are keys, are sorted in ascending order.
    def generate(self, tokenId, currentTime):
        expirationTime = currentTime + self.ttl
        self.tokenToTimeMap[tokenId] = expirationTime # O(1)
        if expirationTime not in self.timeToTokenMap.keys():
            self.timeToTokenMap[expirationTime] = [] # O(logN)
        self.timeToTokenMap[expirationTime].append(tokenId) # O(1)

    def renew(self, tokenId, currentTime):
        if tokenId not in self.tokenToTimeMap:
            return
        oldExpirationTime = self.tokenToTimeMap[tokenId]
        self._invalidateAllExpiredTokens(currentTime)
        newExpirationTime = currentTime + self.ttl
        self.tokenToTimeMap[tokenId] = newExpirationTime
        if oldExpirationTime in self.timeToTokenMap:
            self.timeToTokenMap[oldExpirationTime].remove(tokenId)
        if newExpirationTime not in self.timeToTokenMap:
            self.timeToTokenMap[newExpirationTime] = []
        self.timeToTokenMap[newExpirationTime].append(tokenId)

    def countUnexpiredTokens(self, currentTime):
        self._invalidateAllExpiredTokens(currentTime)
        return len(self.tokenToTimeMap)

    def _invalidateAllExpiredTokens(self, currentTime):
        expired_times = [expiration_time for expiration_time in self.timeToTokenMap if expiration_time <= currentTime]
        for expiration_time in expired_times:
            tokens_to_be_deleted = self.timeToTokenMap.pop(expiration_time)
            for token_id in tokens_to_be_deleted:
                self.tokenToTimeMap.pop(token_id)

        

if __name__ == "__main__":
    # Create an AuthenticationManager with a time-to-live (TTL) of 5 seconds
    auth_manager = AuthenticationManager(timeToLive=5)

    # Generate some tokens
    auth_manager.generate(tokenId="token1", currentTime=1)
    auth_manager.generate(tokenId="token2", currentTime=2)

    # Print the count of unexpired tokens
    print("Unexpired Tokens:", auth_manager.countUnexpiredTokens(currentTime=3))

    # Renew one of the tokens
    auth_manager.renew(tokenId="token1", currentTime=4)

    # Print the count of unexpired tokens after renewal
    print("Unexpired Tokens after Renewal:", auth_manager.countUnexpiredTokens(currentTime=5))
    print("Unexpired Tokens after Renewal:", auth_manager.countUnexpiredTokens(currentTime=6))
    print("Unexpired Tokens after Renewal:", auth_manager.countUnexpiredTokens(currentTime=7))
    print("Unexpired Tokens after Renewal:", auth_manager.countUnexpiredTokens(currentTime=8))
    print("Unexpired Tokens after Renewal:", auth_manager.countUnexpiredTokens(currentTime=9))


"""
Let's analyze the time complexity of each operation:

generate: O(1) - Inserting a new token with its expiration time is a constant time operation. Adding the token to the timeToTokenMap involves appending it to a list.

renew: O(1) - Renewing a token involves updating its expiration time in tokenToTimeMap. Removing it from the old expiration time's list and adding it to the new expiration time's list are constant time operations.

countUnexpiredTokens: O(N) - In the worst case, all tokens are unexpired, and the function needs to iterate through all tokens in tokenToTimeMap.

_invalidateAllExpiredTokens: O(N) - The time complexity depends on the number of expired times in timeToTokenMap. In the worst case, all tokens have expired, and it needs to iterate through all tokens in the expired times.

"""