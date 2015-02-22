from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.conf import settings
from django.core import serializers
from django.http import HttpResponse

from main.models import Album

import json
import sys
import requests

def add_artist(request):
    context = {}
    return render_to_response('add_artist.html', context, context_instance = RequestContext(request))

def browse_artists(request):
    artists = Album.objects.all().values("artistName").distinct()
    context = {'artists' : artists}
    return render_to_response('browse_artists.html', context, context_instance = RequestContext(request))

def update_albums(artist_name):
    r = requests.get('https://itunes.apple.com/search', params={'term':artist_name, 'entity':'album', 'limit':200, 'media':'music', 'attribute':'artistTerm'})
    ret_json = r.json()
    if ret_json['resultCount'] and ret_json['resultCount']>0:
        upper_artist_name = artist_name.upper()
        for result in ret_json["results"]:
            if result["artistName"].upper() == upper_artist_name:
                entry = Album(artistId=result["artistId"],\
                albumId=result["collectionId"],\
                artistName=result["artistName"],\
                albumName=result["collectionName"],\
                artworkUrl100=result["artworkUrl100"],\
                )
                q1 = Album.objects.filter(albumId=result["collectionId"])
                q2 = q1.filter(artistId=result["artistId"])
                if len(q2) == 0:
                    entry.save()



def query(request):
    if request.method == 'POST':
        if "query" in request.REQUEST:
            artist_name = request.REQUEST["query"]
            albums = Album.objects.filter(artistName__iexact=artist_name)
            if len(albums) == 0:
                update_albums(artist_name)
                albums = Album.objects.filter(artistName__iexact=artist_name)
            if len(albums) > 0:
                return HttpResponse("All albums added")
            else:
                return HttpResponse("Artist not found")


def ValuesQuerySet_to_dict(vqs):
    return [item for item in vqs]

def get_albums(request):
    if "artist_name" in request.REQUEST:
        artist_name = request.REQUEST["artist_name"]
        albums = Album.objects.filter(artistName__iexact=artist_name).values("albumName","artworkUrl100")
        result_dict = {"count" : len(albums), "results" : ValuesQuerySet_to_dict(albums)}
        return HttpResponse(json.dumps(result_dict), content_type='json')





