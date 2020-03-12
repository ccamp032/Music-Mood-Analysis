# Music Mood
When people listen to music, certain emotions can be hightened depending on what kind of music is being heard. With this in mind, we extract data from multiple sources. We want to investigate the sentiments of lyrics and what words are being used.

# Phase 1 - Data Acquisition

# Data
We are extracting data from multiple sources for this type of analysis. One source is the [Genius API](https://docs.genius.com/) for the lyrics. Another source is the [Spotify API](https://developer.spotify.com/documentation/web-api/) for various other attributes including genre. Finally, we are scraping data from Wikipedia using [Scrapy](https://scrapy.org/) for various data.

## Genius API
The Genius API is where most of the data is extract from. Below are features that are extracted from this API:

1. Song artist
2. Song title
3. Number of pageviews for the lyric
4. Release data of song
5. How many featured artists
6. Number of words in lyric
7. Song lyrics

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

## Future Attributes
More features we want to add are sentiment extraction scores. Using [NLTK](https://text-processing.com/demo/sentiment/), we will input the lyrics to get a score that represents whether a lyric is deemed positive/negative/neutral. 


# Phase 2 - Data Cleaning & EDA

## Spotify and Genius Data
Data from both API's were grabbed, cleaned and integrated.

### Spotify Data
Data from Spotify was grabbed in bulk. This means that many songs grabbed through Spotify are not in the Genius dataset. Because of this, we needed to find a way to clean and integrate both the Spotify and Genius dataset into one large dataset.

### Cleaning
Data from both Genius and Spotify have track titles. So, the name of a song appears in both API calls. The difference being that in Spotify, the track titles may vary slightly from the track titles from Genius. To combat this, a SequenceMatcher was used. The sequence matcher compared the track title from Genius to a list of songs gathered from Spotify. The match that had the greatest similarity between track titles was used.

### Data Integration
Based on the greatest similarity between track titles, the data from Spotify was concatenated to the current Genius dataset. Now the dataset has additional features from Spotify. Some of the feature descriptions are grabbed straight from the Spotify API. The full list of features are as follow:
1. Song artist
   - **DESCRIPTION**: Name of artist
2. Song title
   - **DESCRIPTION**: Name of song
3. Album Title
   - **DESCRIPTION**: Name of album the song is from.
4. Number of pageviews for the lyric
   - **DESCRIPTION**: Amount of views the lyric page got on the Genius website.
5. Release data of song
   - **DESCRIPTION**: The date the song was released
6. How many featured artists
   - **DESCRIPTION**: The amount of artists featured on song
7. Artist Popularity
   - **DESCRIPTION**: How popular an artist is on Spotify. Range is 0-100.
8. Genre(s)
   - **DESCRIPTION**: Genre the artist is considered as, separated by ' / '.
9. Followers
   - **DESCRIPTION**: The amount of users following an artist on Spotify
10. Danceability
    - **DESCRIPTION**: Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable. (Gotten from Spotify)
11. Energy
    - **DESCRIPTION**: Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.
12. Valence
    - **DESCRIPTION**: A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).
13. Duration (in Milliseconds)
    - **DESCRIPTION**: The length of the song in milliseconds
14. Loudness
    - **DESCRIPTION**: The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typical range between -60 and 0 db.
15. Total words in lyrics
    - **DESCRIPTION**: How many words each lyric has.
16. Lyrics
    - **DESCRIPTION**: The lyrics for the specific song.
## Phase 2 EDA
To find the EDA done by Dark Kit Kat, look in the directory named `Phase_2_data_analysis/`. There are `lyricsDataset.scv` and Jupyter notebook called `LyricDataset_Fin.ipynb` where all the analysis was done by all three members.

## Phase 3 - Data Analysis
We conducted some experiments on which models to use, and which feature combinations work best with these models.
<br>
### Machine Learning Algorithms
Linear Regression <br>
K Nearest Neighbor <br>
Random Forest <br>
Decision Tree <br>
Gradient Boosting <br>
AdaBoost <br>

### Hypothesis 
1. Predicting song track popularity based on its features <br>
2. Predicting song genre based on its features

### Track Popularity Prediction
We used regression algorithm such as linear regression, AdaBoost Regressor,Gradient Boosting Regressor,Decision Tree Regressor, and Voting Regressor on track popularity based on its features.Track popularity prediction is approximating 16 - 17 % accuracy. It wasn't good enough so we decided to use categorical. As a result, we broke popularity into 2 categories : One category that is less 70 is not popular and one category is greater than or equal to 70. Classfiers algorithm such as AdaBoost Classifier and Random Forest Classifier were used to predict the two categories based on its feature importance and cross validation scores. The classifier prediction rates are 92% accuracy. 

### Genre Prediction 
To make a genre prediction, we used four classification algorithms: k-nearest neighbor , Random Forest, AdaBoost , and Decision Tree .
We found the best amount of neighbors is around 36. We used 36 for knn algorithm and used cross validation to find their scores. 
The best knn accuracy for genre is approximately 60%; its not good enough. As a result, we decided to used random forest, adaBoost , and decision tree and used cross validation again to find their scores. Unfortunately , we end up getting approximately the same accuracy as knn which is 60%.

### Result
Song track popularity prediction has a better prediction rate of 92% than genre prediction which is 60%.


### Contributions
**Chris Daniels:** Proposed the hypothesis and used machine learning algorithms to predict genre and popularity. <br>
**Christian Campos:** Used knn algorithm to predict the true genre labels vs predicted genre labels and demonstrated it using confusion matrix. <br>
**Dmitri Koltsov:** Did further analysis on genre and popularity using different machine learning algorithms to find a good prediction rate accuracy to answer the hypothesis. <br>


# Contributors
* Chris Daniels - https://github.com/ChairMane
* Dmitri Koltsov - https://github.com/Dim314159
* Christian Campos - https://github.com/ccamp032

All other known bugs and fixes can be sent to cdani010@ucr.edu , dkolt002@ucr.edu and ccamp032@ucr.edu 

Reported bugs and fixes will be submitted to correction
