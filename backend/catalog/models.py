from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=255, verbose_name="Исполнитель")

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название песни")

    def __str__(self):
        return self.title

class Album(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название альбома")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums', verbose_name="Исполнитель")
    release_year = models.PositiveIntegerField(verbose_name="Год выпуска")
    songs = models.ManyToManyField(Song, through='AlbumTrack', related_name='albums', verbose_name="Песни")
    cover = models.ImageField(upload_to='album-cover/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.release_year})"

class AlbumTrack(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='tracks')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='album_tracks')
    track_number = models.PositiveIntegerField(verbose_name="Порядковый номер")

    class Meta:
        unique_together = ('album', 'track_number')
        ordering = ['track_number']

    def __str__(self):
        return f"{self.track_number}. {self.song.title}"