from django.shortcuts import get_object_or_404, redirect, render
from movies.models import Cast, Genre, Movie
from movies.serializers import CastSerializer, GenreSerializer, MovieSerializer
from rest_framework.views import APIView 
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.urls import reverse
from rest_framework import status


class MovieView(ModelViewSet):
    """
    simple viewset for list post restive update and delete
    """

    serializer_class = MovieSerializer
    queryset = Movie.objects.prefetch_related('genres').all()


class GenereView(ModelViewSet):
    """
    simple viewset for list post restive update and delete
    """

    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class CastView(ModelViewSet):
    """
    simple viewset for list post restive update and delete
    """

    serializer_class = CastSerializer
    queryset = Cast.objects.all()

    
