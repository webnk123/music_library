from rest_framework import serializers
from .models import Artist, Album, Song, SongInAlbum



class ArtistSerializer(serializers.ModelSerializer):
    """
    serialize all artists
    """
    class Meta:
        model = Artist
        fields = ['id', 'artist_name']

class AlbumSerializer(serializers.ModelSerializer):
    """
    serialize all artists
    """
    class Meta:
        model = Album
        fields = ['id','name', 'artist', 'release_year']



class SongSerializer(serializers.ModelSerializer):
    """
    serialize all artists
    """
    class Meta:
        model = Song
        fields = ['id', 'song_name']



class SongInAlbumSerializer(serializers.ModelSerializer):
    """
    serialize all artists
    """
    class Meta:
        model = SongInAlbum
        fields = ['song', 'album','serial_number']
