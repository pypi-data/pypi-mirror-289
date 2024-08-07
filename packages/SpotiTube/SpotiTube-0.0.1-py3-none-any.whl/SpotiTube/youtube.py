from types import NoneType
from pytube import Search
from pytubefix import YouTube
import os

class YTube:

    def __init__(self, downloadPath:str="."):
        self.downloadPath = downloadPath

    def getLink(self, searchQuery:str) -> str:

        results = Search(searchQuery).results
        if results != None and len(results) > 0:
            return results[0].watch_url

        return "Not Found"

    def download(self, link, filename="unknown"):
        self.youtubeObject = YouTube(link)
        self.youtubeObject = self.youtubeObject.streams.get_lowest_resolution()

        if self.youtubeObject is None:
            raise Exception("No Vide Found")

        print("Video File Downloading...")

        self.youtubeObject.download(
            output_path=os.path.join(self.downloadPath),
            filename=filename+".mp4"
        )
        print("Video File Downloaded")
