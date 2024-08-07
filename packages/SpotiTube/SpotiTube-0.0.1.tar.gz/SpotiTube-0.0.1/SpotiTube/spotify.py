import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class Spotify:

    def __init__(self, clientId: str, clientSecret: str) -> None:
        self.clientId = clientId
        self.clientSecret = clientSecret  # Corrected typo
        client_credentials_manager = SpotifyClientCredentials(
            client_id=clientId,
            client_secret=clientSecret
        )

        self.client = spotipy.Spotify(
            client_credentials_manager=client_credentials_manager
        )

    def firstSearch(self, songName: str) -> dict:
        var = self.client.search(songName)["tracks"]["items"][0]  # Corrected typo

        return {
            'name': var['name'],
            'album': var['album']['name'],
            'artist': var['album']['artists'][0]['name'],
            'image': var['album']['images'][0]['url'],
            'metadata': var
        }

    def multipleSearch(self, songName: str) -> list:
        ans = []
        x = self.client.search(songName)["tracks"]["items"]  # Corrected typo

        for var in x:
            ans.append({
                'name': var['name'],
                'album': var['album']['name'],
                'artist': var['album']['artists'][0]['name'],
                'image': var['album']['images'][0]['url'],
            })

        return ans
