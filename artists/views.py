from django.shortcuts import render
from django.views.generic.detail import DetailView

#models
from .models import Artist
# Create your views here.


class ArtistDetailView(DetailView):
    model = Artist

    context_object_name = 'artist'

    def get_template_names(self):
        return 'artist.html'
