from django.test import TestCase
from ..models import Movie, Genere, Cast
from django.utils import timezone
from . import MovieTest
from model_bakery import baker
from pprint import pprint

class MovieTestModels(MovieTest):
    def setUp(self):
        self.movie = baker.make('movies.Movie')
        self.genere = baker.make('movies.Genere', make_m2m=True)
        self.cast = baker.make('movies.Cast', make_m2m=True)
        pprint(self.movie.__dict__)
        pprint(self.genere.__dict__)
        pprint(self.cast.__dict__)

    
    def test_movie_craetion(self):
        movie = self.create_movie()
        self.assertTrue(isinstance(movie, Movie))
        self.assertEqual(str(movie), movie.movie_title)


class GenereTest(TestCase):
    def setUp(self):
        self.genere = baker.make('movies.Genere')
        # pprint(self.genere.__dict__)
    
    def create_genere(self):
        return Genere.objects.create(
            genere_name='Test Genere'
        )
    
    def test_genere_creation(self):
        genere = self.create_genere()
        self.assertTrue(isinstance(genere, Genere))
        self.assertEqual(str(genere), genere.genere_name)



class CastTest(TestCase):
    def setUp(self):
        self.cast = baker.make('movies.Cast')
        # pprint(self.cast.__dict__)

    def create_cast(self):
        return Cast.objects.create(
            cast_name='Test Cast',
            cast_age=20,
            cast_awards='Test Awards'
        )
    
    def test_cast_creation(self):
        cast = self.create_cast()
        self.assertTrue(isinstance(cast, Cast))
        self.assertEqual(str(cast), cast.cast_name)

        