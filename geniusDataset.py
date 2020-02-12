import lyricsgenius as genius
import spotipy as spot
import json
import csv

genius_client_token = json.load(open('config.json'))

class geniusDataset:
    def __init__(self, token):
        self.gen = genius.Genius(token, remove_section_headers=True, timeout=5, excluded_terms=['(Remix)', '(Live)'])

    def getArtist(self, query):
        artist = self.gen.search_artist(query, max_songs=20)
        artist.save_lyrics('{}.json'.format(query.replace(' ', '_')))

    def getAllArtists(self, file):
        with open(file) as artists:
            line = artists.readline()
            while line:
                print(line)
                self.getArtist(line)
                line = artists.readline()
        artists.close()

# Create an API object that makes requests
mood = geniusDataset(genius_client_token['genius_token'])
# Download Json files for all artists in the 'artists' text file
mood.getAllArtists('artists')