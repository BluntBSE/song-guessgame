##Goal: Print a randm song from an artist we give the program to the console

##Log in to spotify - Yes
##Send an artist to Spotify - Yes
##Receive a set of results - Yes
##Pick a random one - Yes
##Print to console - Yes

import spotipy
import random
from spotipy.oauth2 import SpotifyClientCredentials

cid = '31d30a02884f48d98b957108c94ceae4'
secret = 'bf5d73d1e89b4088ae32bc68fd3b9559'

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)


sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

picked_artist = input('Please enter an artist')
song_nums = 10

def get_songs(artist):
    track_names = []
    track_results = sp.search(q="artist:"+artist, type='track', limit=song_nums,offset=0)
    for t in track_results['tracks']['items']:
        track_names.append(t['name']) 
    return track_names

selected_songs = get_songs(picked_artist)

game_song_index = random.randint(0,len(selected_songs)-1)
print(selected_songs[game_song_index])











