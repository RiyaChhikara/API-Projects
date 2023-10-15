# Spotify_API
🎂 This Python script creates a private Spotify playlist with the top songs from Billboard on your birth date. 

## Prerequisites
![spotify Web API ](https://github.com/RiyaChhikara/API-Projects-/assets/115228191/b30df1e1-241e-4ad9-90f1-cce032f1a02b)

Before using this script, you need to have the following:
1. Spotify Developer Account: You should create a Spotify Developer account to obtain the CLIENT_ID and CLIENT_SECRET. Replace these placeholders with your credentials.
2. Spotify Redirect URI: Define a redirect URI when creating your Spotify Developer app, and replace REDIRECT_URI with it.
3. Spotipy Library: Install the Spotipy library, a Python library for the Spotify Web API. You can install it using pip:
  pip install spotipy
4. Beautiful Soup Library: Install the Beautiful Soup library for web scraping. You can install it using pip:
  pip install beautifulsoup4

## Configuration
You need to set the following variables in the script:

- CLIENT_ID: Replace this with your Spotify Developer App's Client ID.
- CLIENT_SECRET: Replace this with your Spotify Developer App's Client Secret.
- REDIRECT_URI: Replace this with the redirect URI associated with your Spotify Developer App.
- URL: This is the URL of the Billboard Hot 100 chart. Ensure that it is up-to-date and points to the correct location.

## Usage
Open a terminal and navigate to the directory containing the Python script.
Run the script using the following command:
python music_player.py

The script will prompt you to enter a date in the format YYYY-MM-DD to specify which year's Billboard Hot 100 chart you want to create a playlist for.
The script will scrape the Billboard chart for that date, search for the songs on Spotify, and create a private playlist with the top 100 songs from that date.

## Customization
You can adjust the Billboard chart URL by modifying the URL variable to point to a different source if needed.

![spotify](https://github.com/RiyaChhikara/API-Projects-/assets/115228191/7de79670-b07d-4547-9387-f5de0dd38869)

## Acknowledgments
This script was created by Riya as a learning project.
If you encounter any issues or have suggestions for improvement, please feel free to file an issue or create a pull request on the GitHub repository.
