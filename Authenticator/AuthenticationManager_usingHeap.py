import heapq

class AuthenticationManager:
    def __init__(self, timeToLive):
        self.ttl = timeToLive
        self.tokenToTimeMap = {}
        self.timeToTokenMap = []

    def generate(self, tokenId, currentTime):
        expirationTime = currentTime + self.ttl
        self.tokenToTimeMap[tokenId] = expirationTime
        heapq.heappush(self.timeToTokenMap, (expirationTime, tokenId))

    def renew(self, tokenId, currentTime):
        if tokenId in self.tokenToTimeMap:
            expirationTime = self.tokenToTimeMap[tokenId]
            self._invalidateAllExpiredTokens(currentTime)
            newExpirationTime = currentTime + self.ttl
            self.tokenToTimeMap[tokenId] = newExpirationTime
            heapq.heappush(self.timeToTokenMap, (newExpirationTime, tokenId))

    def countUnexpiredTokens(self, currentTime):
        self._invalidateAllExpiredTokens(currentTime)
        return len(self.tokenToTimeMap)

    def _invalidateAllExpiredTokens(self, currentTime):
        while self.timeToTokenMap and self.timeToTokenMap[0][0] <= currentTime:
            _, tokenId = heapq.heappop(self.timeToTokenMap)
            del self.tokenToTimeMap[tokenId]

# Example usage:
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
Implementation with a Heap (timeToTokenMap):

generate method:
Time Complexity: O(log N)
renew method:
Time Complexity: O(log N)
countUnexpiredTokens method:
Time Complexity: O(log N)

"""