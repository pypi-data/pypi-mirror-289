import requests
from .youtube import YTube
import os
from moviepy.editor import VideoFileClip
import eyed3
from eyed3.id3.frames import ImageFrame

class Song:

    def __init__(self, metadata:dict, downloadPath:str="."):
        self.metadata = metadata
        self.downloadPath = downloadPath
        self.filename = self.metadata["name"].replace(" ","-").lower()

    def coverArtDownload(self):
        url=self.metadata["image"]
        print("Downloading Cover Art...")
        request = requests.get(url)
        with open(os.path.join(self.downloadPath, f"{self.filename}.jpg"), "wb") as file:
            file.write(request.content)

        print("Cover Art Downloaded")

    def convertVideoToAudio(self):

        print("Converting To Audio...")
        video = VideoFileClip(
            os.path.join(
                self.downloadPath,
                self.filename+".mp4"
            )
        )

        video.audio.write_audiofile(
            os.path.join(
                self.downloadPath,
                self.filename+".mp3"
            )
        )

        os.remove(os.path.join(
            self.downloadPath,
            self.filename+".mp4"
        ))

        print("Converted to Audio Successfully")

    def addMetadataToAudioFile(self):
        audiofile = eyed3.load(
            self.filename+".mp3"
        )
        if (audiofile.tag == None):
            audiofile.initTag()

        audiofile.tag.images.set(
            ImageFrame.FRONT_COVER,
            open(os.path.join(
                self.downloadPath, f'{self.filename}.jpg'),
                'rb').read(),
            'image/jpeg'
        )
        audiofile.tag.artist = self.metadata["artist"]
        audiofile.tag.title = self.metadata["name"]
        audiofile.tag.album = self.metadata["album"]
        audiofile.tag.save()

        os.remove(os.path.join(self.downloadPath, f"{self.filename}.jpg"))

    def __str__(self) -> str:
        return f"{self.metadata['name']} by {self.metadata['artist']}"
