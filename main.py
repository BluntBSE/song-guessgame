##Goal: Print a randm song from an artist we give the program to the console

##Log in to spotify
##Send an artist to Spotify
##Receive a set of results
##Pick a random one
##Print to console---->

import spotipy
import random
from spotipy.oauth2 import SpotifyClientCredentials

cid = '31d30a02884f48d98b957108c94ceae4'
secret = 'bf5d73d1e89b4088ae32bc68fd3b9559'

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)


sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

picked_artist = 'Billie Eilish'

artist_name = []

popularity = []
track_id = []

##TODO: Figure out why the for i in range is a thing. Why is offset i?
def get_songs(artist):
    track_name = []
    for i in range(0,1):
        track_results = sp.search(q="artist:"+artist, type='track', limit=5,offset=i)
        for i, t in enumerate(track_results['tracks']['items']):
            ##artist_name.append(t['artists'][0]['name'])
            track_name.append(t['name'])
           ## track_id.append(t['id'])
            ##popularity.append(t['popularity'])
 
    
    return track_name

selected_songs = get_songs(picked_artist)
print(selected_songs)
game_song_index = random.randint(0,len(selected_songs)-1)
print(selected_songs[game_song_index])


##Here's some hot garbage to demonstrate branches, a function that crashes everything







