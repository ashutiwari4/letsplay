from play.models import ImageDetailsForm, VideoLinksForm
from .models import Genre, Song
from rest_framework.serializers import ModelSerializer


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class ImageDetailsSerializer(ModelSerializer):
    class Meta:
        model = ImageDetailsForm
        fields = '__all__'


class VideoLinkSerializer(ModelSerializer):
    class Meta:
        model = VideoLinksForm
        fields = '__all__'


class SongSerializer(ModelSerializer):
    image = ImageDetailsSerializer(source='imageDetails', many=True, read_only=True)
    video = VideoLinkSerializer(source='videoLink', many=True, read_only=True)

    class Meta:
        model = Song
        fields = '__all__'


class SongLinkList(ModelSerializer):
    class Meta:
        model = ImageDetailsForm
        fields = '__all__'
        # fields = ('id', 'thumbnail')
