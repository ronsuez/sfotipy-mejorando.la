from django.contrib import admin

# Register your models here.

from .models import Album

from tracks.models import Track


class AlbumInLine(admin.StackedInline):
        model = Track


class AlbumAdmin(admin.ModelAdmin):
    inlines = [AlbumInLine, ]



admin.site.register(Album, AlbumAdmin)