import csv

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director

class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_movies = []
        self.__dataset_of_actors = []
        self.__dataset_of_directors = []
        self.__dataset_of_genres = []

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            for row in movie_file_reader:
                title = row['Title']
                release_year = int(row['Year'])
                movie = Movie(title, release_year)
                actors = row['Actors'].split(",")
                directors = Director(row['Director'])
                genres = row['Genre'].split(",")
                if movie not in self.__dataset_of_movies:
                    self.__dataset_of_movies.append(movie)
                else:
                    pass
                if directors not in self.__dataset_of_directors:
                    self.__dataset_of_directors.append(directors)
                else:
                    pass
                for a in actors:
                    actors = Actor(a)
                    if actors not in self.__dataset_of_actors:
                        self.__dataset_of_actors.append(actors)
                    else:
                        pass
                for g in genres:
                    genres = Genre(g)
                    if genres not in self.__dataset_of_genres:
                        self.__dataset_of_genres.append(genres)
                    else:
                        pass
    @property
    def dataset_of_movies(self) -> list:
        return self.__dataset_of_movies
    @property
    def dataset_of_actors(self) -> list:
        return self.__dataset_of_actors
    @property
    def dataset_of_directors(self) -> list:
        return self.__dataset_of_directors
    @property
    def dataset_of_genres(self) -> list:
        return self.__dataset_of_genres




