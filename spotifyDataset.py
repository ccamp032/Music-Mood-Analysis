import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pprint

config = json.load(open("config.json"))

cid = config['spotify_client']
secret = config['spotify_secret']

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def getArtistsAlbums(file):
    # Read txt file of artist names
    artist_dicts = {}
    with open(file) as artists:
        # Read artist name
        line = artists.readline()
        line = line.rstrip('\n')
        while line:
            name, nameID = getNameAndID(line)
            print('Getting info on {}'.format(name))
            artist_dicts[name] = {}
            artist_dicts[name]['artist_id'] = nameID
            artist_dicts[name]['artist_albums'] = getArtistAlbums(nameID)
            artist_dicts[name]['artist_features'] = getArtistPopularity(nameID)
            artist_dicts[name]['artist_tracks'] = getArtistTracks(artist_dicts[name]['artist_albums'])
            artist_dicts[name]['track_features'] = getTrackFeatures(artist_dicts[name]['artist_tracks'])
            line = artists.readline()
            line = line.rstrip('\n')
            print('Done getting info on {}'.format(name))
    print('Finished going through all artists.')
    print('Now saving into json file...')
    artists.close()
    return artist_dicts


def getNameAndID(line):
    if line == 'Tyler, The Creator, 4V8LLVI7PbaPR0K2TGSxFF':
        split = line.split(', ')
        name = split[0] + ', ' + split[1]
        nameID = split[2]
    else:
        split = line.split(', ')
        name = split[0]
        nameID = split[1]
    return name, nameID


def getArtistAlbums(id):
    albums = sp.artist_albums(id)
    items = albums['items']
    album_list = []
    for album in items:
        album_name = album['name']
        album_id = album['id']
        album_list.append((album_name, album_id))

    return album_list


def getArtistTracks(id_dict):
    tracks_list = []
    for album_name, album_id in id_dict:
        tracks = sp.album_tracks(album_id)
        items = tracks['items']
        for track in items:
            track_id = track['id']
            track_name = track['name']
            tracks_list.append((track_name, track_id))

    return tracks_list


def getTrackFeatures(tracks):
    track_features = {}
    for track_name, track_id in tracks:
        track = sp.track(track_id)
        features = sp.audio_features(track_id)
        track_features[track_name] = {}
        try:
            if features == None:
                print('Got an error.')
                track_features[track_name] = {'ERROR': 'No features for this track'}
            else:
                if 'popularity' not in track:
                    track_features[track_name]['popularity'] = 0
                else:
                    track_features[track_name]['popularity'] = track['popularity']
                if 'explicity' not in track:
                    track_features[track_name]['explicit'] = 'NaN'
                else:
                    track_features[track_name]['explicit'] = track['explicit']
                if 'danceability' not in features[0]:
                    track_features[track_name]['danceability'] = 'NaN'
                else:
                    track_features[track_name]['danceability'] = features[0]['danceability']

                if 'energy' not in features[0]:
                    track_features[track_name]['energy'] = 'NaN'
                else:
                    track_features[track_name]['energy'] = features[0]['energy']

                if 'valence' not in features[0]:
                    track_features[track_name]['valence'] = 'NaN'
                else:
                    track_features[track_name]['valence'] = features[0]['valence']

                if 'duration_ms' not in features[0]:
                    track_features[track_name]['duration_ms'] = 'NaN'
                else:
                    track_features[track_name]['duration_ms'] = features[0]['duration_ms']

                if 'loudness' not in features[0]:
                    track_features[track_name]['loudness'] = 'NaN'
                else:
                    track_features[track_name]['loudness'] = features[0]['loudness']
        except:
            print('Had an error inside try/except')
            track_features[track_name] = {'ERROR': 'No features for this track'}
    return track_features


def getArtistPopularity(id):
    artist = sp.artist(id)
    features = {}
    features['artist_popularity'] = artist['popularity']
    features['genre'] = artist['genres']
    features['followers'] = artist['followers']['total']
    return features


def saveJson(spotify_dict):
    with open('spotify_data_updated.json', mode='w') as sd:
        json.dump(spotify_dict, sd)


spot_data = getArtistsAlbums('artistIDs')
saveJson(spot_data)
print('File saved.')


# WHAT HAPPENS:
#  When I run what I have above, I get slowdowns.
#  I get messages like, "retrying ...xsecs"
#  Maybe I am making too many calls.
#  Never mind, it seemed to have worked.