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