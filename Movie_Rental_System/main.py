"""Problem Statement:
You have a movie renting company consisting of n shops. You want to implement a renting system that supports searching for, booking, and returning movies.
The system should also support generating a report of the currently rented movies. Each shop carries at most one copy of a movie moviei.

The system should support the following functions:
Search: Finds the cheapest 5 shops that have an unrented copy of a given movie.
The shops should be sorted by price in ascending order, and in case of a tie, the one with the smaller shop id should appear first. 
If there are less than 5 matching shops, then all of them should be returned. If no shop has an unrented copy, then an empty list should be returned.

Rent: Rents an unrented copy of a given movie from a given shop.

Drop: Drops off a previously rented copy of a given movie at a given shop.

Report: Returns the cheapest 5 rented movies (possibly of the same movie ID) as a 2D list res where res[j] = [shopj, moviej] describes that the jth cheapest rented movie moviej was rented from the shop shopj.
The movies in res should be sorted by price in ascending order, and in case of a tie, the one with the smaller shopj should appear first, and if there is still tie, the one with the smaller moviej should appear first.
If there are fewer than 5 rented movies, then all of them should be returned. If no movies are currently being rented, then an empty list should be returned."""

from movie_rental_system.movieRenting import MovieRentingSystem
n = 4

# [shopid, movieid, price]
movieInfo = [(4, 0, 2),(4, 1, 1), (5, 0, 1), (6, 0, 1)] # ensure Each shop carries at most one copy of a movie.
system = MovieRentingSystem(n, movieInfo)

search_movieid = 0
ans=system.search(0) 
print(f"Available Options for movieId: {search_movieid}")
system.display(ans)

system.rent(4,0)


print("Report:")
report = system.report() 
system.display(report)

system.drop(4, 0)

ans=system.search(0) 
print(f"Available Options for movieId: {search_movieid}")
system.display(ans)  