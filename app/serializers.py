from .models import Artist, Album, Song, SongInAlbum
from rest_framework import serializers


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'artist_name']

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id','name', 'artist', 'release_year']



class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'song_name']



class SongInAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongInAlbum
        fields = ['song', 'album','serial_number']
