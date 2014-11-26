from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
import json
# Create your views here.

#Imported Models
from .models import Track

#look for the track, based on the title passed by url


def classic_view(request, title):
    #Classic try/catch
    try:
        track = Track.objects.get(title=title)
    except Track.DoesNotExist:
        raise Http404

    #First Method to return a response
    return HttpResponse(track.artist)

    #Second Method to return a response and data to a view
    #params : requests, view, data(as a dictionary)
    #return render(request, 'track.html', {'track': track})


def track_view(request, title):

    #A more efficient way

    track = get_object_or_404(Track, title=title)

    #python dictionary
    data = {
        'title': track.title,
        'order': track.order,
        'album': track.album.title,
        'artist': {
            'name': track.artist.first_name,
            'bio': track.artist.bio
        }
    }

    #new json object
    json_data = json.dumps(data)

    return HttpResponse(json_data, content_type='application/json')
