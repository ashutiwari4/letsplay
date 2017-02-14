from play.models import SongDetailsForm
from .models import Genre, Song
from rest_framework.serializers import ModelSerializer


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class SongSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class SongLinkList(ModelSerializer):
    class Meta:
        model = SongDetailsForm
        fields = '__all__'
        # fields = ('id', 'thumbnail')
