from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404
# Create your views here.

#Imported Models
from .models import Track

#look for the track, based on the title passed by url


def track_view(request, title):

   #Classic try/catch

    try:
        track = Track.objects.get(title=title)
    except Track.DoesNotExist:
        raise Http404

    #A more efficient way
    #track = get_object_or_404(Track, title=title)

    #First Method to return a response
    #return HttpResponse(track.artist)

    #Second Method to return a response and data to a view
    # params : requests, view, data(as a dictionary)
    return render(request, 'track.html', {'track': track})
