from django.db import models

# Create your models here.
from artists.models import Artist


class Album(models.Model):
    title = models.CharField(max_length=255)
    #cover = models.ImageField(upload_to='covers')
    artist = models.ForeignKey(Artist)

    #This configures form's field visibility
    def __unicode__(self):
        return self.title