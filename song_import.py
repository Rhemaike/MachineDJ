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
    print("# songs in playlist: ",len(items))

    return songdf


def standardize(row, min,max,avg):
    range  = max - min
    return (row - avg) / range

def minmax_normalize(item, min, max):
    range  = max - min
    return (item - min) / range

def minmax_dfnorm(df, features):
    for feat in features:
        minimum = df[feat].min()
        maximum = df[feat].max()
        df[feat] = df[feat].apply(minmax_normalize, args=[minimum,maximum])
    return df

def stad_dfnorm(df, features):
    for feat in features:
        minimum = df[feat].min()
        maximum = df[feat].max()
        avg = df[feat].mean()
        df[feat] = df[feat].apply(standardize, args=[minimum,maximum,avg])
    
    return df

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
    NN2 = "3ZEIkiOjWSTeNNhix1oGqN"
    NN3 = "6gSTSn9UEj4eV6rENrAl13"
    NN4 = "0QlAmiUtN8AL7M9pjgjvjt"
    NN5 = "2y306QxWv1D8skpMxhogtr"
    NN6 = "571OKYByH4yHYINUbO1M8j"
    NN7 = "2o15TkekA7VuMCcTqHsook"
    NN8 = "3dQioa3CefJs5TD2f6zcHq"
    NN9 = "0GMHKKpNzfwrfIRQagPKHv"
    NN10 = "7fZTtl038X2mnFUTxa06BO"
    test = "71UwSzImcFePNOHMAh3v4h"
    coolvibes= "5M6G2d6F4LIobYnh8Gcjpp"

    P11 = "3TDgf9mn73lqWycaFnJsGF"
    P12 = "1nVtsQyNYOcC608sNkMMHC"
    P13 = "3ZEIkiOjWSTeNNhix1oGqN"

    P21 = "6gSTSn9UEj4eV6rENrAl13"
    P22 = "0QlAmiUtN8AL7M9pjgjvjt"
    P23 = "1x1uzuTgvx8TuiHrUewef5"

    P31 = "3dQioa3CefJs5TD2f6zcHq"
    P32 = "2lGtVufyFMowWQRZhxJHjF"
    P33 = "5oml6NZHKt7ht6iM3mQrj3"

    P41 = "0GMHKKpNzfwrfIRQagPKHv"
    P42 = "7fZTtl038X2mnFUTxa06BO"
    P43 = "2y306QxWv1D8skpMxhogtr"

    playlist_ids = [NN, NN2, NN3, NN4, NN5, NN6, NN7, NN8, NN9, NN10]
    playlist_ids2 = [P11, P12, P13, P21, P22, P23, P31, P32, P33, P41, P42, P43]
    dfs = []
    for play_id in playlist_ids2:
        dfs.append(getfeat_df(play_id))
    
    song_df = pd.concat(dfs)
    
    song_df.to_excel("Song_Feature_Data_set_2.xlsx") 
    new_song_df = song_df[["name", "key", "liveness", "instrumentalness", "loudness", "mode", "speechiness", "tempo", "valence", "danceability", "energy", "acousticness"]].copy()
    new_song_df.to_excel("Song_Feature_Data_set_less_2.xlsx",index=False) 

    # Normalize features
    normfeat = ["key","loudness", "tempo"]
    normdf_minmax = new_song_df
    normdf_minmax = minmax_dfnorm(normdf_minmax, normfeat)
    
    normdf_minmax.to_excel("Song_Feature_Data2_Norm_minmax.xlsx",index=False) 
 


        


