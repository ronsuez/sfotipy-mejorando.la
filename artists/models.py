from django.db import models

# Create your models here.


class Artist(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)

#This configures form's field visibility
    def __unicode__(self):
        return self.first_name + self.last_name

