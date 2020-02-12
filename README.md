# Music Mood
When many people listen to music, certain emotions can be hightened depending on what kind of music is being heard. With this in mind, we grabbed data from multiple sources. We want to correlate the sentiments of lyrics to posts about that specific artist or genre.

# Data
We are grabbing data from multiple sources for this type of analysis. One source is the [Genius API](https://docs.genius.com/) for the lyrics. Another source is the [Spotify API](https://developer.spotify.com/documentation/web-api/) for various other attributes including genre. Finally, we are scraping data from various social media sites using [Scrapy](https://scrapy.org/) for posts about artists in this dataset.

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
So far, the attributes we plan on taking from the Spotify API are genres. We can definitely take as many attributes as we think we can take.

## Scrapy
With Scrapy we plan on grabbing posts that include key words about artists in our dataset. A list of some sites we plan on scraping are:
* Reddit
* Facebook
* Twitter
* Instagram

# Future Attributes
More features we want to add are sentiment extraction scores. Using [NLTK](https://text-processing.com/demo/sentiment/), we will input the lyrics to get a score that represents whether a lyric is deemed positive/negative/neutral. 
