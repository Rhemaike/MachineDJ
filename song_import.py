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

    # ================== Start creating Sond dataframe =====================
    # songdf = pd.DataFrame(columns=["song_title", "tempo", "key", "Genre"])
    # songxl_name = "Billboard_songs_2010-19.xlsx"
    # sng = Song(songxl_name)
    # sngnames = sng.get_names()

    # songdf = pd.DataFrame(columns=["song_title", "key", "artist","tempo"])

    # for name in sngnames:
    #     # print("name is", name)
    #     # print("Song:",name)
    #     key, artist, tempo = get_key(name)
    #     info = {"song_title":name,
    #         "key":key,
    #         "tempo":tempo,
    #         "artist":artist
    #         }
    #     songdf = songdf.append(info,ignore_index=True)

    # songdf.to_excel("output.xlsx") 

    playlist_name = "Neural Beats - Study and Focus"
    # playlist = spotify.search(q="playlist:"+playlist_name,type="playlist")
    # name = "creep"
    # song = spotify.search(q="track:"+name, type='track') 
    # print(playlist)
    # print(song)
    cooljams = "1dku1CDmjYpuXW9m2Zs7ni"
    NN = "7pYSJlHb5THXjtZ1JjHNXX"
    test = "71UwSzImcFePNOHMAh3v4h"
    coolvibes= "5M6G2d6F4LIobYnh8Gcjpp"
    playlist = spotify.playlist(coolvibes)

    # print(playlist)

    # for key,item in playlist.items():
    #     print(key)
    #     if key=="tracks":
    #         for key2,item2 in item.items():
    #             print(key2)
    #             if key2 == "items":
    #                 print("---------------------------------------------")
    #                 for stuff in item2:
    #                     for key3,item3 in stuff.items():
    #                         print("**********************")
    #                         print(key3)
    #                         if key3 == "track":
    #                             print("+++++++++++++++++++++")
    #                             for key4,item4 in item3.items():
    #                                 print(key4)
    #                                 if key4 == "name":
    #                                     print("NAME IS {}".format(item4))
    #                             print("+++++++++++++++++++++")
    #                         print("**********************")
    #                         # print("---------------------------------------------")
    #                         # for key4,item4 in item3.items():
    #                         #     print(key4)
    #                         # print("---------------------------------------------")

    #                 # print(item2)
    #                 print("There are {} tracks".format(len(item2))) 
    #                 # print(item2[0])
                        

    #                 print("---------------------------------------------")
    #         print()

    items = playlist["tracks"]["items"]
    for item in items:
        print("Name is song: {}".format(item["track"]["name"]))
        print("id is: {}".format(item["track"]["id"]))
        song_id = item["track"]["id"]

    song = spotify.track(song_id)
    # print(song)
    aud = spotify.audio_analysis(song_id)
    track = aud['track']
    ft = spotify.audio_features(song_id)
    f1 = ft[0]
    # print(track)
    features = ["key",  "mode",  "time_signature", "acousticness", "danceability", "energy", 
    "instrumentalness", "liveness","loudness", "speechiness", "valence", "tempo"]
    for key, item in f1.items():
        print(key)
    for feature in features:
        print(f1[feature])

    # tracks = spotify.playlist_tracks(NN)
    # print(len(tracks["items"]))

        


