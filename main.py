# import tornado
# import tornado.simple_httpclient
#
# httpclient = tornado.simple_httpclient.SimpleAsyncHTTPClient()
#
# username = 'harry.hedges'
# password = 'mhuk1234'


import spotipy
from spotipy.oauth2 import SpotifyOAuth
from haikufy import Haikufy

client_id = '87e6350d94b0498ea12ef96f0da77f91'
client_secret = '8cd177fc383344dd8ba7d7a2d468d077'
redirect = 'http://localhost:8888'


scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect,
                                               scope=scope))


results = sp.user_playlist_tracks('harry.hedges', '3WZIaulqNSqXO49uOJx1ou')
tracks = results['items']
while results['next']:
    results = sp.next(results)
    tracks.extend(results['items'])

# print(tracks)
results = tracks
track_names = []
for track in list(map(lambda x: x['track']['name'], results)):
    if (')' in track) or ('(' in track) or ('.' in track) or ('-' in track):
        continue
    track_names += [track]
print(track_names)
haiku = Haikufy(track_names)
print(haiku.haiku)




