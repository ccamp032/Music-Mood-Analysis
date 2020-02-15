from pathlib import Path
import json


def generateStrings():
    list_of_urls = []
    with open('URLS.txt', 'a') as urls:
        paths = Path('artist_jsons').glob('**/*.json')

        for path in paths:
            # Turn path object into string
            artist_json = str(path)

            with open(artist_json) as json_file:
                data = json.load(json_file)
                for song in data['songs']:
                    if 'path' not in song:
                        list_of_urls.append('WWOOOOOOOOOOOOOOOOOOOOOOOOOOOPS \n')
                    else:
                        list_of_urls.append('genius.com' + song['path'] + ' \n')
            json_file.close()
        urls.writelines(list_of_urls)
    urls.close()


generateStrings()
