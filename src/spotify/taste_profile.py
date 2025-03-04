"""
Module for the Taste Profile class.
"""
from src.spotify.client import spotify_client


class TasteProfile:
    """
    A class representing a user's taste profile
    """
    def __init__(self):
        self.sp = spotify_client
        self.profile_dict = {}
        self.get_taste_profile("medium_term", 50)

    def get_taste_profile(self, time_range: str, limit: int):
        """
        Method that generates a user's taste profile by scanning their top songs and top artists.
        :param time_range: A string representing the time range.
        Valid strings include 'short_term' (4 weeks), 'medium_term' (6 months), and 'long_term' (all data)
        :param limit: limit of artists and tracks returned
        :return:
        """
        top_artists_data = self.sp.current_user_top_artists(time_range=time_range, limit=limit)
        top_tracks_data = self.sp.current_user_top_tracks(time_range=time_range, limit=limit)

        # Get the users top genres
        genres = [g for artist in top_artists_data['items'] for g in artist['genres']]
        counts = {}
        for genre in genres:
            if genre not in counts:
                counts[genre] = 0
            counts[genre] += 1

        top_genres = []
        for genre, frequency in counts.items():
            top_genres.append(
                {
                    'genre_name': genre,
                    'frequency': frequency
                }
            )
        top_genres.sort(key=lambda item: item['frequency'], reverse=True)

        # Simplify the structure of the top artists and tracks
        top_artists = [artist["name"] for artist in top_artists_data['items']]
        top_tracks = [
            {
                'name': track['name'],
                'artist': track['artists'][0]['name']
            }
            for track in top_tracks_data['items']
        ]
        taste_profile = {
            'time_range': time_range,
            'top_artists': top_artists,
            'top_tracks': top_tracks,
            'top_genres': top_genres
        }
        self.profile_dict = taste_profile
