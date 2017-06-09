import fresh_tomatoes
import media

# 3 Movie objects
toy_story = media.Movie("Toy Story", "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

bahubali = media.Movie("Bahubali", "https://upload.wikimedia.org/wikipedia/en/7/7e/Baahubali_poster.jpg",
                       "https://www.youtube.com/watch?v=sOEg_YZQsTI")

matrix_1 = media.Movie("The Matrix (1999)", "http://ia.media-imdb.com/images/M/MV5BMTkxNDYxOTA4M15BMl5BanBnXkFtZTgwNTk0NzQxMTE@._V1_.jpg",
                       "https://www.youtube.com/watch?v=vKQi3bBA1y8")

# created a list of Movie objects
movies = [toy_story, avatar, bahubali]

fresh_tomatoes.open_movies_page(movies)
