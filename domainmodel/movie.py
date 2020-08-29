from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director

class Movie:
    def __init__(self, title: str, release_yr: int):
        if title == "" or type(title) != str:
            self.__title = None
        else:
            self.__title = title.strip()
        if release_yr >= 1900:
            self.__release_yr = release_yr
        else:
            self.__release_yr = None
        self.__description: str = None
        self.__director: Director = None
        self.__actors = []
        self.__genres = []
        self.__runtime_minutes: int = 0
    @property
    def title(self) -> str:
        return self.__title
    @title.setter
    def title(self, title: str):
        if title == "" or not isinstance(title, str):
            self.__title = None
        else:
            self.__title = title.strip()
    @property
    def release_year(self) -> int:
        return self.__release_yr
    @release_year.setter
    def release_year(self, yr: int):
        if self.__release_yr >= 1900 and isinstance(yr, int):
            self.__release_yr = yr
    @property
    def description(self) -> str:
        return self.__description
    @description.setter
    def description(self, description: str):
        if isinstance(description, str) and description != "":
            self.__description = description
        else:
            self.__description = None
    @property
    def director(self)->Director:
        return self.__director
    @director.setter
    def director(self, director: 'Director'):
        if isinstance(director, Director):
            self.__director = director
        else:
            raise TypeError
    @property
    def actors(self) -> list:
        return self.__actors
    @actors.setter
    def actors(self, actor_li: list):
        if isinstance(actor_li, list):
            self.__actors += actor_li
    @property
    def genres(self) -> list:
        return self.__genres
    @genres.setter
    def genres(self, genres_li: list):
        if isinstance(genres_li, list):
            self.__genres += genres_li
    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes
    @runtime_minutes.setter
    def runtime_minutes(self, mins: int):
        if mins >= 0:
            self.__runtime_minutes = mins
        else:
            raise ValueError
    def __repr__(self) -> str:
        return "<Movie {}, {}>".format(self.__title, self.__release_yr)
    def __eq__(self, other: 'Movie') -> bool:
        return (self.__title == other.__title) and (self.__release_yr == other.__release_yr)
    def __lt__(self, other:'Movie') -> bool:
        if self.__title < other.__title:
            return True
        elif self.__title == other.__title:
            return self.__release_yr < other.__release_yr
        else:
            return False
    def __hash__(self):
        return hash((self.__title, self.__release_yr))
    def add_actor(self, actor: 'Actor'):
        if isinstance(actor, Actor):
            self.actors.append(actor)
        else:
            raise TypeError
    def remove_actor(self, actor: 'Actor'):
        if isinstance(actor, Actor):
            if actor in self.__actors:
                self.__actors.remove(actor)
            else:
                pass
        else:
            raise TypeError
    def add_genre(self, genre: 'Genre'):
        if isinstance(genre, Genre):
            self.__genres.append(genre)
        else:
            raise TypeError
    def remove_genre(self, genre:'Genre'):
        if isinstance(genre, Genre):
            if genre in self.__genres:
                self.__genres.remove(genre)
            else:
                pass
        else:
            raise TypeError



