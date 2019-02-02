from movie import Movie
from serie import Serie
from playlist import PlayList

movie = Movie('Fast & Furios 8',2017,107)
serie = Serie('The Blindspot', 2015, 4)

movie.give_like()
movie.give_like()

serie.give_like()

playlist = PlayList("Favorites",[movie,serie])

print(movie in playlist)

for program in playlist:
    print(program)

print(f'The size of playlist is {len(playlist)}')
