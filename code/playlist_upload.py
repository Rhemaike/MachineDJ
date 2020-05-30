scope = 'playlist-modify-public'
# 658eab07309b4d11846fa3636413a425
# 6b1d14ccfccc4c1bb74d08542337ce1f
# http://localhost:4000
import sys
import spotipy
import spotipy.util as util

# scope = 'user-library-read'

# if len(sys.argv) > 1:
#     username = sys.argv[1]
# else:
#     print("Usage: %s username" % (sys.argv[0],))
#     sys.exit()
username='rhemaike'
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    name = "Test user creator playlist"
    playlist = sp.user_playlist_create(username, name, public=True, description='')
    playlist_id = playlist["id"]  # Get playlist ID 
    # Add track to playlist
    # tracks = [] # list of track URIs, URLs or IDs
    # user_playlist_add_tracks(username, playlist_id, tracks, position=None)
else:
    print("Can't get token for", username)