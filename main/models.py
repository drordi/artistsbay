from django.db import models

class Album(models.Model):
  artistId = models.BigIntegerField()
  albumId = models.BigIntegerField()
  artistName = models.CharField(max_length=200)
  albumName = models.CharField(max_length=200)
  artworkUrl100 = models.URLField(max_length=200)


