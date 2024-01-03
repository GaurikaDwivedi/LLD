class AuthenticationManager:
    def __init__(self, timeToLive):
        self.ttl = timeToLive
        self.unexpiredTokens = {} # maps unexpired tokens to their expiration time

    def generate(self, tokenId, currentTime):
        # O(1)
        # generates a new token with the given tokenId at the given currentTime in seconds.
        self.unexpiredTokens[tokenId] = currentTime + self.ttl

    def renew(self, tokenId, currentTime):
        # O(N)
        # renews the unexpired token with the given tokenId at the given currentTime in seconds.
        # If there are no unexpired tokens with the given tokenId, the request is ignored, and nothing happens.
        self.invalidateAllExpiredTokens(currentTime)  # as per requirements: if a token expires at time t, and another action happens on time t (example: request to renew the token or
                                                      # request to get count of unexpired tokens in the system), the expiration takes place before the other actions.
                                                      # O(N) operation
        if tokenId in self.unexpiredTokens.keys():
            self.unexpiredTokens[tokenId] = currentTime + self.ttl # O(1)

    def countUnexpiredTokens(self, currentTime): # O(N)
                                                # returns the number of unexpired tokens at the given currentTime.
        self.invalidateAllExpiredTokens(currentTime) # as per requirements: if a token expires at time t, and another action happens on time t (example: request to renew the token or
                                                    #  request to get count of unexpired tokens in the system), the expiration takes place before the other actions.
                                                    # O(N) operation 
        return len(self.unexpiredTokens)

    #  evict all expired tokens
    def invalidateAllExpiredTokens(self, currentTime): # O(N), where N = total number of tokens  present in the system. This includes both unexpired tokens and also expired but still not evicted tokens at time currentTime
        tokensToBeDeleted = []
        for token, expiration_time in self.unexpiredTokens.items():
            if expiration_time <= currentTime:
                tokensToBeDeleted.append(token)
        for token in tokensToBeDeleted: # O(N)
            self.unexpiredTokens.pop(token)
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
