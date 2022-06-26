from django.test import TestCase
from ..models import Movie, Genere, Cast
from django.utils import timezone

class MovieTest(TestCase):

    def create_movie(self):
        return Movie.objects.create(
            movie_title='Test Movie',
            movie_description='Test Description',
            release_date=timezone.now()
        )


    def create_genere(self):
        return Genere.objects.create(
            genere_name='Test Genere'
        )


    def create_cast(self):
        return Cast.objects.create(
            cast_name='Test Cast',
            cast_age=20,
            cast_awards='Test Awards'
        )