from pathlib import Path
from difflib import SequenceMatcher
import json
import csv

class Dataset:
    def __init__(self, directory, spot_file=None):
        self.directory = directory
        self.spot_file = spot_file
        self.spotify_data = json.load(open(self.spot_file))

    # Grab json files from directory
    def getJsonData(self):
        paths = Path(self.directory).glob('**/*.json')

        for path in paths:
            # Turn path object into string
            artist_json = str(path)
            # Send string into generation function
            self.generateData(artist_json)

    def generateData(self, file):
        row = []
        # Read passed in file to generate CSV file
        with open(file) as json_file:
            data = json.load(json_file)
            self.generateCSV(row, data)
        json_file.close()

    def matchTracks(self, genius_track, spotify_tracks):
        max = 0
        correct_track = ''
        for track in spotify_tracks:
            ratio = SequenceMatcher(None, genius_track.lower(), track.lower()).ratio()
            if ratio > max:
                max = ratio
                correct_track = track
        return correct_track

    def generateCSV(self, row, data):
        if data['name'] == 'Beyoncé':
            NAME = 'Beyonce'
        else:
            NAME = data['name']
        #print(NAME)
        artist_data = self.spotify_data[NAME]
        spotify_artist_songs = list(artist_data['track_features'].keys())
        artist_features = artist_data['artist_features']
        track_features = artist_data['track_features']
        for song in data['songs']:
            cor_track = self.matchTracks(song['title'], spotify_artist_songs)
            if cor_track == '':
                features = {}
            else:
                features = track_features[cor_track]
            # These if statements are here for
            # empty fields
            # If name is not a field, replace with 'NaN'
            if 'name' not in data:
                row.append('NaN')
            else:
                row.append(data['name'])
            # If title is not a field, replace with 'NaN'
            if 'title' not in song:
                row.append('NaN')
            else:
                row.append(song['title'])

            if 'album' not in song:
                row.append('NaN')
            else:
                albumname = song['album']
                if albumname == None:
                    row.append('NaN')
                else:
                    row.append(song['album']['name'])
            # If pageviews is not a field, replace with 0
            if 'pageviews' not in song['stats']:
                row.append(0)
            else:
                row.append(song['stats']['pageviews'])
            # If release_date is not a field, replace with 'NaN'
            if 'release_date' not in song:
                row.append('NaN')
            else:
                row.append(song['release_date'])
            # If featured_artists is not a field, replace with -1
            if 'featured_artists' not in song:
                row.append(-1)
            else:
                row.append(len(song['featured_artists']))

            if 'artist_popularity' not in artist_features:
                row.append(0)
            else:
                row.append(artist_features['artist_popularity'])

            if 'genre' not in artist_features:
                row.append('NaN')
            else:
                row.append(' / '.join(artist_features['genre']))

            if 'followers' not in artist_features:
                row.append(0)
            else:
                row.append(artist_features['followers'])

            # IF danceability is not a field, replace with -1
            if 'danceability' not in features:
                row.append(-1)
            else:
                row.append(features['danceability'])
            if 'popularity' not in features:
                row.append(-1)
            else:
                row.append(features['popularity'])
            if 'explicit' not in features:
                row.append('NaN')
            else:
                row.append(features['explicit'])
            # IF energy is not a field, replace with -1
            if 'energy' not in features:
                row.append(-1)
            else:
                row.append(features['energy'])

            # IF valence is not a field, replace with -1
            if 'valence' not in features:
                row.append(-1)
            else:
                row.append(features['valence'])

            # IF duration is not a field, replace with 0
            if 'duration_ms' not in features:
                row.append(0)
            else:
                row.append(features['duration_ms'])

            # IF loudness is not a field, replace with 999
            if 'loudness' not in features:
                row.append(999)
            else:
                row.append(features['loudness'])

            # If lyrics is not a field, replace with 0 and 'NaN'
            if 'lyrics' not in song:
                row.append(0)
                row.append('NaN')
            else:
                row.append(len(song['lyrics'].split()))
                row.append(song['lyrics'].replace(',', ' '))

            # Append json data to given csv file
            with open('lyricDataset.csv', mode='a') as lyric_file:
                lyric_writer = csv.writer(lyric_file, delimiter=',')
                lyric_writer.writerow(row)
            row.clear()
        lyric_file.close()

CSV = Dataset('artist_jsons', 'spotify_data_updated.json')
CSV.getJsonData()