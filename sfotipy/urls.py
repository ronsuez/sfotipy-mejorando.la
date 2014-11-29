from django.conf.urls import patterns, include, url
from django.contrib import admin
from artists.views import ArtistDetailView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sfotipy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^tracks/(?P<title>[\w\-]+)', 'tracks.views.track_view', name='track_view'),
    url(r'^signup/', 'user_profile.views.signup', name='signup'),
    url(r'^signin/', 'user_profile.views.signin', name='signin'),
    url(r'^artist/(?P<pk>[\d]+)', ArtistDetailView.as_view()),

)
