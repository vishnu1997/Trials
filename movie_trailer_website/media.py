""" Movie class 

     Attributes - 
       movie_title - Will store the title of movie,
       poster_image_url - url of the poster,
       trailer_youtube_url - trailer of the movie link 
"""
class Movie: 

    #Constructor 
    def __init__(self, movie_title, poster_image_url, trailer_youtube_url):
        self.movie_title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

#end of class