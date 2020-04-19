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


def getfeat_df(playlist_name):
    # Create df with features:
    features = ["key",  "mode",  "time_signature", "acousticness", "danceability", "energy", 
    "instrumentalness", "liveness","loudness", "speechiness", "valence", "tempo","name"]
    songdf = pd.DataFrame()

    # Find the tracks in playlist
    playlist = spotify.playlist(playlist_name)
    items = playlist["tracks"]["items"]
    song_ids = []
    song_names = []
    for item in items:
        name = item["track"]["name"]
        songid  = item["track"]["id"]
        # print("Name is song: {}".format(name))
        # print("id is: {}".format(songid))
        song_ids.append(songid)
        song_names.append(name)

    feat_list = spotify.audio_features(song_ids)

    for feat,name in zip(feat_list,song_names):
        feat_dic = feat
        feat_dic["name"] = name
        songdf = songdf.append(feat_dic,ignore_index=True)

    return songdf
            

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

    #============================ CREATE DF WITH SONGS FROM PLAYLIST AND FEATURES ==============================

    playlist_name = "Neural Beats - Study and Focus"
    cooljams = "1dku1CDmjYpuXW9m2Zs7ni"
    NN = "7pYSJlHb5THXjtZ1JjHNXX"
    test = "71UwSzImcFePNOHMAh3v4h"
    coolvibes= "5M6G2d6F4LIobYnh8Gcjpp"

    playlist_ids = [NN, coolvibes, test, cooljams ]
    dfs = []
    for play_id in playlist_ids:
        dfs.append(getfeat_df(play_id))
    
    song_df = pd.concat(dfs)
    
    song_df.to_excel("Song_data_2.xlsx") 
    new_song_df = song_df[["name", "key", "liveness", "instrumentalness", "loudness", "mode", "speechiness", "tempo", "valence", "danceability", "energy", "acousticness"]].copy()
    new_song_df.to_excel("Song_data_2_less.xlsx",index=False) 
    

    # # Find the tracks in playlist
    # items = playlist["tracks"]["items"]
    # song_id = [0]* len(items)
    # for item in items:
    #     print("Name is song: {}".format(item["track"]["name"]))
    #     print("id is: {}".format(item["track"]["id"]))
    #     song_id = item["track"]["id"]

    # song = spotify.track(song_id)
    # # print(song)
    # aud = spotify.audio_analysis(song_id)
    # track = aud['track']
    # ft = spotify.audio_features(song_id)
    # f1 = ft[0]
    # # print(track)
    # features = ["key",  "mode",  "time_signature", "acousticness", "danceability", "energy", 
    # "instrumentalness", "liveness","loudness", "speechiness", "valence", "tempo"]
    # for key, item in f1.items():
    #     print(key)
    # for feature in features:
    #     print(f1[feature])



        


