tools = [
    {
        "name": "build_playlist",
        "description": "Builds a playlist using the Spotify API (spotipy). The 'songs' parameter must be a dictionary with song names as keys and artist names as values. You must provide it.",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "The name for the playlist"
                },
                "songs": {
                    "type": "array",
                    "description": "A list of songs and artists that are pipe delimited (|)",
                    "items": {
                        "type": "string"
                    }
                },
                "description": {
                    "type": "string",
                    "description": "A description for the playlist"
                }
            }
        }
    }
]

