"""
@/**************************************************/@
Developed By Snehashish Laskar (github handle: @snehashish090)
Package Development Started On : 7th August 2024
Barebones version (v0.0.1) with limited functionality
@/**************************************************/@
"""

from .youtube import *
from .song import *
from .spotify import *

class Downloader:

    """
    Object to bring everything together
    Spotify Object from spotify.py file needs to be initialised with credentials first
    """
    def __init__(
        self,
        downloadPath,
        spotifyClient:Spotify,
    ):
        self.downloadPath = downloadPath
        self.spotifyClient = spotifyClient

    def downloadSong(self, songTitle:str, raw=False):
        try:
            songDetails = self.spotifyClient.firstSearch(songTitle)
        except Exception as ex:
            raise Exception("Fetching song from spotify not successfull:", ex)

        song = Song(
            metadata=songDetails,
            downloadPath=self.downloadPath
        )
        try:
            song.coverArtDownload()
        except Exception as ex:
            raise Exception("Downloading Cover Art Failed:", ex)

        try:
            ytDownloader = YTube(self.downloadPath)
            searchQuery = f'{song.metadata["artist"]} - {song.metadata["name"]}  {song.metadata["album"]} official audio'
            link = ytDownloader.getLink(searchQuery)
            ytDownloader.download(link, filename=song.filename)
        except Exception as ex:
            raise Exception("Youtube Download Failed:", ex)

        try:
            song.convertVideoToAudio()
        except Exception as ex:
            raise Exception(f"Could'nt Convert video to audio : {ex}")

        try:
            song.addMetadataToAudioFile()
        except Exception as ex:
            raise Exception(f"Adding metadata to audio file failed: {ex}")

        print("Successfully Downloaded")

        if raw:
            with open(os.path.join(song.downloadPath, song.filename+".mp3"), "rb")as file:
                x = file.read()
                os.remove(os.path.join(song.downloadPath, song.filename+".mp3"))
                return x
        else:
            return os.path.join(
                song.downloadPath,
                song.filename+".mp3"
            )
