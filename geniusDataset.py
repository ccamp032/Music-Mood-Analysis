import lyricsgenius as genius
from pathlib import Path
import string
import json

# Grab token from config file
genius_client_token = json.load(open('config.json'))

class geniusDataset:
    def __init__(self, token):
        # Create Genius API object
        self.gen = genius.Genius(token, remove_section_headers=True, timeout=5, excluded_terms=['(Remix)', '(Live)'])

    def getArtist(self, query):
        # Only grab 20 songs per artist
        artist = self.gen.search_artist(query, max_songs=20)
        # Create json file with artist name
        artist.save_lyrics('{}.json'.format(query.replace(' ', '_')))

    def getAllArtists(self, file):
        # Read txt file of artist names
        with open(file) as artists:
            # Read artist name
            line = artists.readline()
            line = line.rstrip('\n')
            while line:
                # Send artist name as a query for Genius API
                if self.checkArist(line):
                    line = artists.readline()
                    line = line.rstrip('\n')
                else:
                    self.getArtist(line)
                    line = artists.readline()
                    line = line.rstrip('\n')
        artists.close()

    # Check if artist in file already exists
    def checkArist(self, name):
        if Path('artist_jsons/{}.json'.format(name.replace(' ', '_').replace(',', '').replace('(', '').replace(')', '').replace('!', '').replace('-', '').replace('/', ''))).is_file():
            print('Already retrieved data for {}.'.format(name.replace(' ', '_').replace(',', '').replace('(', '').replace(')', '')))
            return True
        else:
            print('Data for {} not retrieved yet, Retrieving now...'.format(name.replace(' ', '_').replace(',', '').replace('(', '').replace(')', '').replace('/', '')))
            return False

# Create an API object that makes requests
mood = geniusDataset(genius_client_token['genius_token'])
# Download Json files for all artists in the 'artists' text file
mood.getAllArtists('artists_test')