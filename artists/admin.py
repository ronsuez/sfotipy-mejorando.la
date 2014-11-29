from django.contrib import admin

# Register your models here.

from .models import Artist
from albums.models import Album


class AlbumInLine(admin.StackedInline):
        model = Album


class ArtistAdmin(admin.ModelAdmin):
        inlines = [AlbumInLine, ]

admin.site.register(Artist, ArtistAdmin)




