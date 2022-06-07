from django.shortcuts import render

def MovieView(request):
    return render(request, 'movie.html')
