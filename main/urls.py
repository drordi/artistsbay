from django.conf.urls import patterns, url

from main import views

urlpatterns = patterns('',
    url(r'^$', views.add_artist, name='add_artist'),
    url(r'^add_artist$', views.add_artist, name='add_artist'),
    url(r'^browse_artists$', views.browse_artists, name='browse_artists'),
    url(r'^query$', views.query, name='query'),
    url(r'^get_albums$', views.get_albums, name='get_albums'),
)
