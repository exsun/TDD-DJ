from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers



# router = routers.DefaultRouter()
# router.register(r'movies', views.MovieView)
# router.register(r'genres', views.GenereView)
# router.register(r'casts', views.CastView)

# # MovieGener
# movie_genre = routers.NestedDefaultRouter(router, r'movies', views.MovieView, lookup='movies')
# movie_genre.register(r'genres', views.GenereView, basename="movie_genre")

# urlpatterns = router.urls + movie_genre.urls

app_name="movies"

urlpatterns = [
    path(r'movies/', views.MovieView.as_view({'get': 'list', 'post': 'create'}), name="movie_list"),
    path(r'movies/<int:pk>/', views.MovieView.as_view({'get': 'retrieve', 'delete': 'destroy'}), name="movie_detail"),
    path(r'genres/', views.GenereView.as_view({'get': 'list', 'post': 'create'}), name="genre_list"),
    path(r'genres/<int:pk>/', views.GenereView.as_view({'get': 'retrieve', 'delete': 'destroy'}), name="genre_detail"),
    path(r'casts/', views.CastView.as_view({'get': 'list', 'post': 'create'}), name="cast_list"),
    path(r'casts/<int:pk>/', views.CastView.as_view({'get': 'retrieve', 'delete': 'destroy'}), name="cast_detail"),
]