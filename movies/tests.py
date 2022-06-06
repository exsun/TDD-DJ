from django.test import TestCase
from .models import Movie, Genere, Cast
from django.utils import timezone

class MovieTest(TestCase):

    def create_movie(self):
        return Movie.objects.create(
            movie_name='Test Movie',
            movie_description='Test Description',
            release_date=timezone.now()
        )
    
    def test_movie_craetion(self):
        movie = self.create_movie()
        self.assertTrue(isinstance(movie, Movie))
        self.assertEqual(str(movie), movie.movie_name)


class GenereTest(TestCase):
    
    def create_genere(self):
        return Genere.objects.create(
            genere_name='Test Genere'
        )
    
    def test_genere_creation(self):
        genere = self.create_genere()
        self.assertTrue(isinstance(genere, Genere))
        self.assertEqual(str(genere), genere.genere_name)



class CastTest(TestCase):

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

        