# Music Mood
When many people listen to music, certain emotions can be hightened depending on what kind of music is being heard. With this in mind, we grabbed data from multiple sources. We want to investigate the sentiments of lyrics and what words are being used.

# Data
We are grabbing data from multiple sources for this type of analysis. One source is the [Genius API](https://docs.genius.com/) for the lyrics. Another source is the [Spotify API](https://developer.spotify.com/documentation/web-api/) for various other attributes including genre. Finally, we are scraping data from Wikipedia using [Scrapy](https://scrapy.org/) for various data.

## Genius API
The Genius API is where the bulk of the data comes from. Below are features that are grabbed from this API:

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

## Crawling and Scraping
With Scrapy and BeautifulSoup, we are scraping tables off of Wikipedia pages. For example, here is a link we scraped for album data: https://en.wikipedia.org/wiki/Eminem_albums_discography

From these tables, we plan on creating a dataset with these features:
1. Artist Name
2. Album Name
3. Sales (From various different countres)
4. Amount of certifications

# Future Attributes
More features we want to add are sentiment extraction scores. Using [NLTK](https://text-processing.com/demo/sentiment/), we will input the lyrics to get a score that represents whether a lyric is deemed positive/negative/neutral. 

# Contributors
* Chris Daniels
* Dmitri Koltsov
* Christian Campos
