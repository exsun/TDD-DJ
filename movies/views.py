from django.shortcuts import get_object_or_404, redirect, render
from movies.models import Movie
from movies.serializers import MovieSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.urls import reverse
from rest_framework import status


class MovieListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'movie.html'

    def get(self, request):
        queryset = Movie.objects.all()
        return Response({'movies': queryset})


    
