from rest_framework import serializers
from .models import Album,Band,Genre


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class RegisterGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'