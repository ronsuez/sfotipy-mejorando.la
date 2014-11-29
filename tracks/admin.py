from django.contrib import admin

# Register your models here.

from .models import Track


class TrackAdmin(admin.ModelAdmin):
    list_display = ('order', 'album', 'title', 'artist', 'player')
    list_filter = ('artist', 'album')
    search_fields = ('artist__first_name', 'artist__last_name', 'album__title')
    list_editable = ('title', 'album', 'artist')



admin.site.register(Track, TrackAdmin)