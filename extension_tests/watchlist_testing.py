import pytest
from domainmodel.movie import Movie
from domainmodel.watchlist import WatchList


@pytest.fixture()
def watchlist():
    return WatchList()


def test_init(watchlist):
    assert watchlist.size() == 0


def test_size(watchlist):
    watchlist.add_movie(Movie("SAW I", 2001))
    watchlist.add_movie(Movie("SAW II", 2002))
    watchlist.add_movie(Movie("SAW III", 2003))
    watchlist.add_movie(Movie("SAW IV", 2004))
    watchlist.add_movie(Movie("SAW V", 2005))
    assert watchlist.size() == 5
    watchlist.remove_movie(Movie("SAW I", 2001))
    assert watchlist.size() == 4
    watchlist.add_movie(Movie("SAW I", 2001))
    assert watchlist.size() == 5


def test_add_movies(watchlist):
    watchlist.add_movie(Movie("SAW I", 2001))
    watchlist.add_movie(Movie("SAW II", 2002))
    watchlist.add_movie(Movie("SAW III", 2003))
    watchlist.add_movie(Movie("SAW IV", 2004))
    watchlist.add_movie(Movie("SAW V", 2005))
    assert watchlist.size() == 5
    watchlist.add_movie(Movie("SAW VI", 2006))
    assert watchlist.size() == 6
    watchlist.add_movie(Movie("SAW V", 2005))
    assert watchlist.size() == 6


def test_remove_movie(watchlist):
    watchlist.add_movie(Movie("SAW I", 2001))
    watchlist.add_movie(Movie("SAW II", 2002))
    watchlist.add_movie(Movie("SAW III", 2003))
    watchlist.add_movie(Movie("SAW IV", 2004))
    watchlist.add_movie(Movie("SAW V", 2005))
    watchlist.remove_movie(Movie("SAW IV", 2004))
    watchlist.remove_movie((Movie("SAW II", 2002)))
    assert watchlist.size() == 3
    watchlist.remove_movie(Movie("SAW X", 2010))
    assert watchlist.size() == 3


def test_first_movie_to_watch(watchlist):
    watchlist.add_movie(Movie("SAW I", 2001))
    watchlist.add_movie(Movie("SAW II", 2002))
    watchlist.add_movie(Movie("SAW III", 2003))
    watchlist.add_movie(Movie("SAW IV", 2004))
    watchlist.add_movie(Movie("SAW V", 2005))
    assert watchlist.first_movie_in_watchlist() == Movie("SAW I", 2001)
    watchlist.remove_movie(Movie("SAW I", 2001))
    assert watchlist.first_movie_in_watchlist() == Movie("SAW II", 2002)


def test_movie_to_watch_index(watchlist):
    watchlist.add_movie(Movie("SAW I", 2001))
    watchlist.add_movie(Movie("SAW II", 2002))
    watchlist.add_movie(Movie("SAW III", 2003))
    watchlist.add_movie(Movie("SAW IV", 2004))
    watchlist.add_movie(Movie("SAW V", 2005))
    assert watchlist.select_movie_to_watch(0) == Movie("SAW I", 2001)
    assert watchlist.select_movie_to_watch(4) == Movie("SAW V", 2005)


def test_movie_to_watch_outOfIndex(watchlist):
    watchlist.add_movie(Movie("SAW I", 2001))
    watchlist.add_movie(Movie("SAW II", 2002))
    watchlist.add_movie(Movie("SAW III", 2003))
    watchlist.add_movie(Movie("SAW IV", 2004))
    watchlist.add_movie(Movie("SAW V", 2005))
    assert watchlist.size() == 5
    assert watchlist.select_movie_to_watch(6) == None
    assert watchlist.select_movie_to_watch(-1) == None


def test_iterate_movie_list(watchlist):
    watchlist.add_movie(Movie("SAW I", 2001))
    watchlist.add_movie(Movie("SAW II", 2002))
    watchlist.add_movie(Movie("SAW III", 2003))
    watchlist.add_movie(Movie("SAW IV", 2004))
    watchlist.add_movie(Movie("SAW V", 2005))
    temp = iter(watchlist)
    assert watchlist.size() == 5
    assert next(temp) == Movie("SAW I", 2001)
    assert next(temp) == Movie("SAW II", 2002)
    assert next(temp) == Movie("SAW III", 2003)
    assert next(temp) == Movie("SAW IV", 2004)
    assert next(temp) == Movie("SAW V", 2005)


def test_iterate_last_element_movie_list(watchlist):
    watchlist.add_movie(Movie("SAW I", 2001))
    watchlist.add_movie(Movie("SAW II", 2002))
    watchlist.add_movie(Movie("SAW III", 2003))
    watchlist.add_movie(Movie("SAW IV", 2004))
    watchlist.add_movie(Movie("SAW V", 2005))
    temp = iter(watchlist)
    length = watchlist.size()
    last_movie = watchlist.select_movie_to_watch(length - 1)
    assert next(temp) == Movie("SAW I", 2001)
    assert next(temp) == Movie("SAW II", 2002)
    assert next(temp) == Movie("SAW III", 2003)
    assert next(temp) == Movie("SAW IV", 2004)
    assert next(temp) == last_movie












