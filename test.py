import webbrowser


class Movie:
    """
    1. A class to define details for movies
    2. Inputs: movie_title, storyline, poster_image, trailer_youtube
    3. Outputs: -
    """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """

        :param movie_title: string - title of movie
        :param movie_storyline: string - brief story of movie
        :param poster_image: url - image of dvd cover
        :param trailer_youtube: url - trailer of film
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        #self.director = director

    # def show_info(self):
    #     print("Title: " + self.title)
    #     print("Storyline: " + self.storyline)
    #     print("Director: " + self.director)

    # def open_trailer(self):
    #    trailer_movie = webbrowser.open(self.trailer_youtube_url)
