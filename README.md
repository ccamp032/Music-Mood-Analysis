# Music Mood
When people listen to music, certain emotions can be hightened depending on what kind of music is being heard. With this in mind, we extract data from multiple sources. We want to investigate the sentiments of lyrics and what words are being used.

# Phase 1 - Data Acquisition

# Data
We are extracting data from multiple sources for this type of analysis. One source is the [Genius API](https://docs.genius.com/) for the lyrics. Another source is the [Spotify API](https://developer.spotify.com/documentation/web-api/) for various other attributes including genre. Finally, we are scraping data from Wikipedia using [Scrapy](https://scrapy.org/) for various data.

## Genius API
The Genius API is where most of the data is extract from. Below are features that are extracted from this API:

1. Song artist
2. Song title
3. Song lyrics
4. Number of words in lyric
5. Number of pageviews for the lyric
6. Release date of song
7. How many featured artists

## Spotify API
From the Spotify API, we plan on getting a few features. Below are features that are planned:

8. Popularity (Scale from 0-100)
9. Genre
10. Explicit lyrics (True/False)
11. Duration of song (in milliseconds)
12. Various extra features [Spotify track features](https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/)


## Web Scaping and Crawler
We're using Scrapy to scrape album tables from Wikipedia pages. For example, here is a link we scraped for album data: https://en.wikipedia.org/wiki/Eminem_albums_discography  Then we're using BeautifulSoup to parse every table in the json file to create CSV file from json. Below are the scraping and parsing procedure:

1. Scrape tables from Wiki pages using Scrapy
2. Get HTML of tables in Json format using Scrapy
3. Parse every table in the json file using BeautifulSoup
4. Create separate json file with chosen data from table 
5. Create CSV file from json file

From the parse table, we plan on creating a csv dataset with these features:
1. Artist Name
2. Album Name
3. US Sales 

# Future Attributes
More features we want to add are sentiment extraction scores. Using [NLTK](https://text-processing.com/demo/sentiment/), we will input the lyrics to get a score that represents whether a lyric is deemed positive/negative/neutral. 

# Contributors
* Chris Daniels - https://github.com/ChairMane
* Dmitri Koltsov - https://github.com/Dim314159
* Christian Campos - https://github.com/ccamp032

All other known bugs and fixes can be sent to cdani010@ucr.edu , dkolt002@ucr.edu and ccamp032@ucr.edu 

Reported bugs and fixes will be submitted to correction
