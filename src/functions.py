from src.spotify.playlist import Playlist


def convert_to_dict(song_list):
    """
    Converts a list of pipe-delimited strings, where each string is in the format "song|artist",
    into a dictionary with the song as the key and the artist as the value.

    Parameters:
    song_list (list of str): A list where each string is a song and artist separated by a pipe.

    Returns:
    dict: A dictionary mapping songs to artists.
    """
    song_dict = {}
    for entry in song_list:
        # Split the string by the pipe delimiter
        parts = entry.split('|')
        if len(parts) == 2:
            song, artist = parts
            # Use strip to remove any leading/trailing whitespace
            song_dict[song.strip()] = artist.strip()
        else:
            # Handle unexpected formats by raising an error or you can choose to ignore the entry
            raise ValueError(f"Entry '{entry}' is not in the expected 'song|artist' format.")
    return song_dict


def build_playlist(args):
    name = args[0][1]
    songs = convert_to_dict(args[1][1])
    description = args[2][1]
    playlist = Playlist(name, songs, description)
    return playlist.send_playlist_to_spotify()

