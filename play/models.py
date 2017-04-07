from __future__ import unicode_literals

from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.


class Genre(models.Model):
    gid = models.IntegerField()
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=200)
    movie = models.CharField(max_length=200, blank=True)
    lyrics = RichTextField(config_name='awesome_ckeditor', blank=True)
    tabs = RichTextField(config_name='awesome_ckeditor', blank=True)
    chords = RichTextField(config_name='awesome_ckeditor')
    tags = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre)

    def __str__(self):
        return self.name


class LinkType(models.Model):
    source = models.CharField(max_length=20)
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.source


class ImageDetailsForm(models.Model):
    thumbnail = models.CharField(max_length=300)
    image_url = models.CharField(max_length=300)
    image_encoding = models.CharField(max_length=20)
    accent_color = models.CharField(max_length=10)
    name = models.ForeignKey(Song, related_name='imageDetails')


class VideoLinksForm(models.Model):
    link = models.CharField(max_length=300)
    type = models.ForeignKey(LinkType)
    name = models.ForeignKey(Song, related_name='videoLink')
