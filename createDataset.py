from pathlib import Path
import json
import csv

class Dataset:
    def __init__(self, directory):
        self.directory = directory

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

    def generateCSV(self, row, data):
        for song in data['songs']:
            #print(song.keys())
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
                print('In here')
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

CSV = Dataset('artist_jsons')
CSV.getJsonData()