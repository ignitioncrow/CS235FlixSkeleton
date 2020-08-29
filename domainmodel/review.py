from datetime import datetime

from domainmodel.movie import Movie

class Review:
    def __init__(self,movie: 'Movie', review_text: str, rating: int):
        self.__movie: Movie = movie
        if review_text == "" or type(review_text) is not str:
            self.__review_text = None
        else:
            self.__review_text: str = review_text
        if rating >= 1 and rating <= 10:
            self.__rating = rating
        else:
            self.__rating = None
        self.__timestamp = datetime.today()
    @property
    def movie(self):
        return self.__movie
    @movie.setter
    def movie(self, movie: 'Movie'):
        if isinstance(movie, Movie):
            self.__movie = movie
        else:
            raise TypeError
    @property
    def review_text(self) -> str:
        return self.__review_text
    @review_text.setter
    def review_text(self, txt: str):
        if txt == "" or type(txt) is not str:
            self.__review_text = None
        else:
            self.__review_text = txt
    @property
    def rating(self) -> int:
        return self.__rating
    @rating.setter
    def rating(self, score):
        if type(score) == int:
            if score >= 1 and score <= 10:
                self.__rating = rating
            else:
                self.__rating = None
        else:
            raise TypeError
    @property
    def timestamp(self):
        return self.__timestamp
    @timestamp.setter
    def timestamp(self, time):
        self.__timestamp = time
    def __repr__(self) -> str:
        return "Review: {}, {}".format(self.__review_text, self.__rating)
    def __eq__(self, other: 'Review'):
        return self.__review_text == other.__review_text and self.__movie == other.__movie and \
            self.__rating == other.__rating and self.__timestamp == other.__review_text



