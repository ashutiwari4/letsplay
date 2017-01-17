from django.http import HttpResponse
from django.template import loader
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

from .serializers import *
from .models import Genre, Song


# Create your views here.


def index(request):
    template = loader.get_template('index.html')
    context = {
        'genres': Genre.objects.all(),
    }
    return HttpResponse(template.render(context, request))


def song(request, id):
    template = loader.get_template('song.html')
    context = {
        'song': Song.objects.get(id=id)
    }
    return HttpResponse(template.render(context, request))


# api/

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class GenreList(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = StandardResultsSetPagination


class SongList(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    pagination_class = StandardResultsSetPagination
