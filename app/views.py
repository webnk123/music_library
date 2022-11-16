from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Artist, Album, Song, SongInAlbum
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer, SongInAlbumSerializer




# CRUD operations for artists, albums and songs


class ArtistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows artists to be viewed or edited.
    """
    queryset = Artist.objects.all().order_by('artist_name')
    serializer_class = ArtistSerializer
    http_method_names = ['get', 'post', 'delete', 'patch', 'head']


class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Albums to be viewed or edited.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    http_method_names = ['get', 'post', 'delete', 'patch', 'head']


class SongViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Songs to be viewed or edited.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    http_method_names = ['get', 'post', 'delete', 'patch', 'head']







@api_view(['DELETE'])
def RemoveFromAlbum(request, alb_id, sng_id):
    """
    remove song from album
    """
    try:
        song = SongInAlbum.objects.filter(song=sng_id).filter(album=alb_id)
    except SongInAlbum.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if song:
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


class AddToAlbum(generics.CreateAPIView):
    """
    add song to album (with serial number)
    """
    serializer_class = SongInAlbumSerializer



class AlbumsByArtist(generics.ListAPIView):
    """
    A view to get all albums by an artist (by id)
    """
    serializer_class = AlbumSerializer

    def get_queryset(self):

        artist = self.kwargs['artist']

        return Album.objects.filter(artist=artist)



class SongsByAlbum(generics.ListAPIView):
    """
    A view to get all songs in an album by album id
    """
    serializer_class = SongInAlbumSerializer

    def get_queryset(self):

        album = self.kwargs['album']
        sia = SongInAlbum.objects.filter(album=album)

        return sia
