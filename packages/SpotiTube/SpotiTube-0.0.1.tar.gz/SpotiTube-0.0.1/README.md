# Spotify Song Downloader

## Description
This package allows users to download songs from Spotify by searching for song titles and retrieving them via YouTube. It combines Spotify's search functionality with YouTube's video downloading capabilities to provide a seamless music downloading experience.

## Features
- Search for songs using Spotify's extensive database
- Download songs as MP3 files
- Automatically add metadata (artist, album, title) to downloaded files
- Include album artwork in the MP3 file

## Installation
(Instructions for installation will go here once the package is published)

## Usage

### Basic Usage
```python
from spotify_song_downloader import Downloader, Spotify

# Initialize Spotify client
spotify_client = Spotify(
    clientId="your_spotify_client_id",
    clientSecret="your_spotify_client_secret"
)

# Create Downloader object
downloader = Downloader("path/to/download/directory", spotify_client)

# Download a song
downloader.downloadSong("Song Title")
