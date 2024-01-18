from movie_rental_system.movie import Movie
import heapq

class MovieRentingSystem:
    
    # movieInfo[i] = [shopid, movieid, price]
    def __init__(self, n, movieInfo):
        self.rented_heap = [] # to generate report
        self.unrented = {} # movieId -> {shopId -> [(price, movie)]}
        self.resultSetSize = 5
        for entry in movieInfo:
            shopId = entry[0]
            movieId = entry[1]
            price = entry[2]
            mov = Movie(movieId, shopId, price)
            # put the movie in unrented data structures
            heapq.heappush(self.unrented.setdefault(movieId, {}).setdefault(shopId, []), (price, mov))
        
    def search(self, movieId):
        res = []
        count = self.resultSetSize
        if movieId not in self.unrented.keys():
            return res
        availableCopies = heapq.nsmallest(self.resultSetSize, self.unrented[movieId].values(), key=lambda x: x[0])
        for copies in availableCopies:
            for price, movie in copies:
                 if count < 1:
                    break
            res.append(movie)
            count -= 1
        return res
    
    def rent(self, shopId, movieId):
        if movieId not in self.unrented or shopId not in self.unrented[movieId]:
            print(f"Movie: {movieId} is not available in shop: {shopId}.\n")
            return False

        min_price, movie = heapq.heappop(self.unrented[movieId][shopId])
        heapq.heappush(self.rented_heap, (min_price, movie))
        print(f"Movie: {movieId} successfully rented from shop: {shopId}.\n")
        return True

    def drop(self, shopId, movieId):
        movieToReturn = None
        for i,(price, movie) in enumerate(self.rented_heap):
            if movie._id == movieId and movie.getShopId() == shopId:
                movieToReturn = movie
                del self.rented_heap[i]
                break
        if movieToReturn is not None:
            heapq.heappush(self.unrented[movieId][shopId], (movieToReturn._price, movieToReturn))
            print(f"Movie: {movieId} successfully dropped in shop: {shopId}.\n")
        else:
            print(f"Movie: {movieId} was not rented from shop: {shopId}.\n")
            
    def report(self):
        ans = []
        for i in range(min(self.resultSetSize, len(self.rented_heap))): 
        #The loop runs for a number of iterations equal to the minimum of self.resultSetSize and the length of self.rented_heap. 
        #This ensures that the loop doesn't exceed the size of the rented heap or the desired report size.
            price, movie = self.rented_heap[i]
            ans.append(movie)
        return ans
        
    def display(self, ans):
        for movie in ans:
            print(f"ShopId: {movie.getShopId()}, movieid: {movie.id}, Price: {movie._price}")
        print()