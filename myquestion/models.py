from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Playlist(models.Model):
    user = user = models.OneToOneField(User,related_name='playlists', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    @property
    def songs_total_length(self) -> int:
        return sum([song.length for song in self.songs.all()])

    def __str__(self) -> str:
        return self.name


class Song(models.Model):
    playlist = models.ForeignKey(Playlist, related_name='songs', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    length = models.PositiveIntegerField(help_text=('In seconds'))

    def __str__(self) -> str:
        return self.title   