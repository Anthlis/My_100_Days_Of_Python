import requests
import uplink

from uplink_helpers import raise_for_status

@uplink.json
@raise_for_status
class MovieSearchClient(uplink.Consumer):

    def __init__(self):
        super().__init__(base_url='http://movie_service.talkpython.fm')


    @uplink.get('/api/search/run')
    def all_entries(self) -> requests.models.Response:
        """ Get's all movies from the server. """


    @uplink.get('/api/search/{keyword}')
    def search_movies_by_keyword(self, keyword) -> requests.models.Response:
        """ Search for a movie using a keyword. """


    @uplink.get('/api/search/{director_name}')
    def search_movies_by_director(self, director_name) -> requests.models.Response:
        """ Search for a movie by director. """


    @uplink.get('/api/search/{imdb_number}')
    def search_movies_by_imdb(self, imdb_number) -> requests.models.Response:
        """ Search for a movie by IMDB code. """

