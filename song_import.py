#Author: Rhema Ike


# imports
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

from exform import Song

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
letterkey = {
            0:"C",
            1:"C#/Db",
            2:"D",
            3:"D#/Eb",
            4:"E",
            5:"F",
            6:"F#/Gb",
            7:"G",
            8:"G#/Ab",
            9:"A",
            10:"A#/Bb",
            11:"B"
        }

def get_key(name):
    try:
        song = spotify.search(q="track:"+name, type='track')            

        songInfo = song['tracks']['items'][0]

        song_id = 0
        artist = ""
        print("\n============= Song Item {} ================".format(name))
        for key,item in songInfo.items():
            # print(key)
            if key == "id":
                # print("id is ", item)
                song_id = item
            if key=="artists":
                # print(item)
                artist = item

        aud = spotify.audio_analysis(song_id)
        # print("================== Aud nalysis ======================")

        # for key,item in aud.items():
        #     print(key)

        track = aud['track']

        # for key,item in track.items():
        #     print(key)
        #     if key == "key":
        #         print("key info ", item)

        track_key = track["key"]
        tempo =  track["tempo"]
        artist = artist[0]["name"]
        print("The key of song is:{}, tempo is {}, artist is {}".format(letterkey[track_key], tempo, artist) )
        return letterkey[track_key], artist, tempo
    except Exception as e:
        print(e)
        return None,None,None


if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = ' '.join(sys.argv[1:])
    else:
        name = 'Radiohead'

    # results = spotify.search(q='artist:' + name, type='artist')
    # items = results['artists']['items']
    # if len(items) > 0:
    #     artist = items[0]
        # print(artist['name'], artist['images'][0]['url'])
        # print(artist)

    ## STUFF NOW IN GET SONG KEY USED TO BE HERE



    # ================== Start creating Sond dataframe =====================
    songdf = pd.DataFrame(columns=["song_title", "tempo", "key", "Genre"])
    # print(songdf)
    songxl_name = "Billboard_songs_2010-19.xlsx"
    sng = Song(songxl_name)
    sngnames = sng.get_names()

    songdf = pd.DataFrame(columns=["song_title", "key", "artist","tempo"])

    for name in sngnames:
        # print("name is", name)
        # print("Song:",name)
        key, artist, tempo = get_key(name)
        info = {"song_title":name,
            "key":key,
            "tempo":tempo,
            "artist":artist
            }
        songdf = songdf.append(info,ignore_index=True)
        
    # name = "shake it out"
    # spotify = get_key(name)
    songdf.to_excel("output.xlsx") 
        


