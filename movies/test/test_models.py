from django.test import TestCase
from ..models import Movie, Genre, Cast
from django.utils import timezone
from . import TestSetUp
from pprint import pprint

class MovieTestModels(TestSetUp):
    def test_movie_craetion(self):
        
        self.assertTrue(isinstance(self.movie, Movie))


class GenreTest(TestSetUp):
    def test_genre_creation(self):
    
        self.assertTrue(isinstance(self.genre, Genre))



class CastTest(TestSetUp):    
    def test_cast_creation(self):

        self.assertTrue(isinstance(self.cast, Cast))

        