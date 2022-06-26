from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers



router = routers.DefaultRouter()
router.register(r'movies', views.MovieView)
router.register(r'genres', views.GenereView)
router.register(r'casts', views.CastView)

# MovieGener
movie_genre = routers.NestedDefaultRouter(router, r'movies', views.MovieView, lookup='movies')
movie_genre.register(r'genres', views.GenereView, basename="movie_genre")

urlpatterns = router.urls + movie_genre.urls