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
    release_year = models.PositiveIntegerField()

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
    serial_number = models.PositiveIntegerField()

    class Meta:
        # one album cant have same song twice unique_together = (song, album)
        # one album can't have same serial number twice unique together = (album, serial_number)
        unique_together = (("song", "album"),("album", "serial_number"))
        ordering = ['serial_number']
