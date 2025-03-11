"""
Module that handles the Spotify API client.
"""
import os
import spotipy
from spotipy import SpotifyOAuth


scope = 'user-library-read, user-top-read, playlist-modify-private'

spotify_client = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIFY_URI")
    )
)