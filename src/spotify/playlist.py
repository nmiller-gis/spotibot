"""
Module which controls playlist creation and management
"""
from src.spotify.client import spotify_client


class Playlist:
    def __init__(self, name: str, songs: dict, description: str = None):
        self.songs = songs
        self.name = name
        self.description = description

    def _search_for_songs(self) -> list:
        track_ids = []
        for song, artist in self.songs.items():
            query = f"track:{song} artist:{artist}"
            results = spotify_client.search(q=query, type='track', limit=1)
            tracks = results.get('tracks', {}).get('items', [])
            if tracks:
                track_id = tracks[0]['id']
                track_ids.append(track_id)

        return track_ids

    def send_playlist_to_spotify(self):
        track_ids = self._search_for_songs()
        playlist = spotify_client.user_playlist_create(
            user=spotify_client.current_user()['id'],
            name=self.name,
            public=False,
            description=self.description
        )
        playlist_id = playlist['id']

        for i in range(0, len(track_ids), 100):
            spotify_client.user_playlist_add_tracks(
                user=spotify_client.current_user(),
                playlist_id=playlist_id,
                tracks=track_ids[i:i+100]
            )

        return {
            "songs": self.songs,
            "name": self.name,
            "description": self.description,
            "result": "The playlist was successfully created with the given parameters above!"
        }
