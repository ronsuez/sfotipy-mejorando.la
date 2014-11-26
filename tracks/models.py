from django.db import models

# Create your models here.

from albums.models import Album
from artists.models import Artist


class Track(models.Model):
    title = models.CharField(max_length=255)
    #file = models.FileField(upload_to='tracks')
    order = models.PositiveIntegerField()
    album = models.ForeignKey(Album)
    artist = models.ForeignKey(Artist)

#This configures form's field visibility
    def __unicode__(self):
        return self.title