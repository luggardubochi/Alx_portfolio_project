#!/usr/bin/env python
import os
import azapi
import spotipy
from tinytag import TinyTag
from spotipy.oauth2 import SpotifyClientCredentials

def get_spotify():
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
            client_id=os.getenv("client_id"),
            client_secret=os.getenv("clent_secret")
        )
    )

    results = sp.search(q='weezer', limit=20)
    for idx, track in enumerate(results['tracks']['items']):
        print(idx, track['name'])
        for key, value in track.items():
            print(F"\t\t\t{key}, {value}")

def generate_audiometadata(name_of_music):
    """
        Function for generating the metadata

        Args:
            name_of_music: This is the music actively playing
    """
    audio = TinyTag.get(name_of_music)
    return audio.title, audio.artist

def generate_lyrics(title, artist):
    try:
        info = azapi.AZlyrics()
        info.artist = artist
        info.title = title
        lyrics = info.getLyrics()
    except Exception as e:
        lyrics = "No Internet connection\nConnect to a reliable internet source"
    return lyrics