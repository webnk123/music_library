from django.db import models


class Artist(models.Model):
    artist_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.artist_name

    class Meta:
        verbose_name_plural = "Artists"
        ordering = ['id']


class Album(models.Model):
    name = models.CharField(max_length=255, unique=True)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    release_year = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Albums"
        ordering = ['id']


class Song(models.Model):
    song_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.song_name

    class Meta:
        verbose_name_plural = "Songs"
        ordering = ['id']



class SongInAlbum(models.Model):
    song = models.ForeignKey('Song', on_delete=models.CASCADE)
    album = models.ForeignKey('Album', on_delete=models.CASCADE, related_name='songs')
    # album can't have 2 songs with same serial number
    serial_number = models.PositiveIntegerField(unique=True)

    class Meta:
        # one album cant have same song at different serial numbers
        unique_together = (("song", "album"),)
        ordering = ['serial_number']

