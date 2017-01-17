from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=200)
    tabs_and_chords = models.TextField()
    tags = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre)

    def __str__(self):
        return self.name
