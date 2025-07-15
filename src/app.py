import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dotenv import load_dotenv
import spotipy

load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(auth_manager=auth_manager)

artist_id = "spotify:artist:6M2wZ9GZgrQXHCFfjv46we" 

results = spotify.artist_top_tracks(artist_id)
top_tracks = results['tracks']

tracks_data = {
    
    'Album Name': [track['album']['name'] for track in top_tracks],
    'Artist Name':[track['artists'][0]['name'] for track in top_tracks],
    'Track Name': [track['name'] for track in top_tracks],
    'Popularity': [track['popularity'] for track in top_tracks],
    'Album Release Date': [track['album']['release_date'] for track in top_tracks],

}

tracks_df = pd.DataFrame(tracks_data)

top_10_songs = tracks_df.nlargest(10, 'Popularity')

plt.figure(figsize=(12, 6))
plt.style.use('dark_background')
sns.barplot(x='Popularity', y='Track Name', hue='Track Name' , data=top_10_songs, palette='Greens', label=False)
plt.title('Top 10 Tracks of Dua Lipa')
plt.xlabel('Popularity')
plt.ylabel('Track Name')
plt.gca().invert_yaxis()
plt.xticks(rotation=0)
plt.savefig('Top 10 Tracks of Dua Lipa.png')
plt.show()

top_3_albums = tracks_df['Album Name'].value_counts().head(3)

plt.figure(figsize=(8, 7))
sns.barplot(x=top_3_albums.index, y=top_3_albums.values, hue=top_3_albums.values, data=top_10_songs[:3], palette='Greens', legend=False)
plt.title('Top 3 Albums of Dua Lipa')
plt.xlabel('Album Name')
plt.ylabel('Number of Tracks')
plt.xticks(rotation=0)
plt.savefig('Top 3 Albums of Dua Lipa.png')
plt.show()