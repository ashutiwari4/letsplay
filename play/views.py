from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination


from .serializers import *
from .models import Genre, Song
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def index(request):
    queryset = Genre.objects.all()
    paginator = Paginator(queryset, 10)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'genres': queryset,
    }
    return render(request, 'index.html', context)


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


class SongLinkList(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongLinkList
    pagination_class = StandardResultsSetPagination
