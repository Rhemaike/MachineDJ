#Author: Rhema Ike
# imports
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import os

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
    song_artists = []
    for item in items:
        name = item["track"]["name"]
        songid  = item["track"]["id"]
        artist = item["track"]["artists"][0]["name"]
        # print("Name is song: {}".format(name))
        # print("id is: {}".format(songid))
        song_ids.append(songid)
        song_names.append(name)
        song_artists.append(artist)

    feat_list = spotify.audio_features(song_ids)

    for feat,name,artist in zip(feat_list,song_names,song_artists):
        feat_dic = feat
        feat_dic["name"] = name
        feat_dic["artist"] = artist
        songdf = songdf.append(feat_dic,ignore_index=True)
    print("# songs in playlist: ",len(items))

    return songdf


def standardize(row, min,max,avg):
    range  = max - min
    return (row - avg) / range

def minmax_normalize(item, min, max):
    try:
        range  = max - min
        return (item - min) / range
    except Exception as e:
        print(e)
        print("min max item:",min,max,item)
        exit(3)


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
    P14 = "1RegbWk6Uj2lQYfaLDnZzp"
    P15 = "56mKPrUGL6RwLQ2GoEyVnM"
    P16 = "2eXsFfIUzVRepYmJ49OTrs"
    P17 = "0R1zMACNQ9Nala5T5ViJl1"
    P18 = "01Pd2HVvXYOJUC7bIdYdF1"
    P19 = "0vf2Np2mY5wVLAfWFP67XG"
    P110 = "1CPEKrwbhSTAQ2PhA7GGoZ"


    P21 = "6gSTSn9UEj4eV6rENrAl13"
    P22 = "0QlAmiUtN8AL7M9pjgjvjt"
    P23 = "1x1uzuTgvx8TuiHrUewef5"
    P24 = "54fJ9GHAMGkmH3EW2T7Emm"
    P25 = "3SzMrSo8NK1SMnv1mPy6Rx"
    P26 = "0EFaxFWwWWx35NoicVvUIj"
    P27 = "75ACiTPkvbcq4eWYJ33ngr"
    P28 = "1dv03ubPD72hFaJbUzMM8G"
    P29 = "4egO459iQdhUotMcPg15cQ"
    P210 = "1lsnPKl6gDoN0H72sN4MVG"

    P31 = "3dQioa3CefJs5TD2f6zcHq"
    P32 = "2lGtVufyFMowWQRZhxJHjF"
    P33 = "5oml6NZHKt7ht6iM3mQrj3"
    P34 = "7aBu2zQxTdzj0MfNqoQCwv"
    P35 = "2sQ2NlMNWlAZ6layISaOLK"
    P36 = "5c0JRlRcrcVEqOr0aQkHod"
    P37 = "1VleJtMH7tAtsi2sNVQqxa"
    P38 = "5b9CQSmHSRwjyY9haI84rA"
    P39 = "29Wztm9runyFIOik4LfVXW"
    P310 = "6mj3mNH7bcsCFSd4tE2vmW"

    P41 = "0GMHKKpNzfwrfIRQagPKHv"
    P42 = "7fZTtl038X2mnFUTxa06BO"
    P43 = "2y306QxWv1D8skpMxhogtr"
    P44 = "7Gve87oAvrTLSxe62IlnPB"
    P45 = "1NwUJ3JFrmVNx5tTQoyld1"
    P46 = "343Sa7FScLtCgb1esNrPY6"
    P47 = "15UaUb2NAEEXBjarMOVBBj"
    P48 = "7l2VYrWywwQS847QjNTl3E"
    P49 = "30V3Qq6PAddNxXPIvxrP7P"
    P410 = "0Dp1zVCoSElGGrbhZsocqb"

    T1 = "25o3QaP7TsE6oVpEpNXbiS"
    T2 = "2vxkHrAfOjYFPOUu8zDVOS"
    T3 = "6UKetNyN1Jihb5XzROpSX0"
    T4 = "1ieD4bKwTnJBVzjqtR52WW"
    T5 = "7w8ALECJYQWYCdvhsZ32ld"
    T6 = "3MK5jNWfOZsJF8g1diJfiA"
    T7 = "5xcr7ulWMefHitEvEIE6rY"
    T8 = "0y28Z0z2GKZGoQ15tEJWGi"
    T9 = "1HiCZa1XOMHg4a3BuDS4ga"
    T10 = "1GVXbD0Wgp8OXbcZTCVH3g"
    T11 = "3n618x9eeMJYju0QDAqQff"
    T12 = "5iQeBH8kzvg6T1AOPL6VlU"
    T13 = "7ttRIJMhqkvfnQieSZFRyV"
    T14 = "7wNdoi3sg6Y9ziFMOn7uQo"
    T15 = "2bfgrtagHiRoBBT6xA701X"
    T16 = "7Ih9Xx6VrDkG1opuKdRZn3"
    T17 = "56mKPrUGL6RwLQ2GoEyVnM"
    T18 = "3SzMrSo8NK1SMnv1mPy6Rx"
    T19 = "5c0JRlRcrcVEqOr0aQkHod"
    T20 = "2y306QxWv1D8skpMxhogtr"
    


    playlist_ids = [NN, NN2, NN3, NN4, NN5, NN6, NN7, NN8, NN9, NN10]
    playlist_ids2 = [P11, P12, P13, P14, P15, P16, P17, P18, P19, P110,
                    P21, P22, P23, P24, P25, P26, P27, P28, P29, P210,
                    P31, P32, P33, P34, P35, P36, P37, P38, P39, P310,
                    P41, P42, P43, P44, P45, P46, P47, P48, P49, P410]
    playlist_ids3 = [T1, T2, T3, T4, T5, T6, T7, T8, T9, T10,
                        T11,T12,T13,T14,T15,T16,T17,T18,T19,T20]
    dfs = []
    for play_id in playlist_ids2:
        dfs.append(getfeat_df(play_id))
    
    song_df = pd.concat(dfs)
    
    file_name1 = "TestSongDataSet.xlsx"
    file_name2 = "TestSongDataSetLess.xlsx"
    file_name3 = "TestSongMinMax.xlsx"

    DATA_DIR = "DataSets"

    file_name1 = os.path.join(DATA_DIR, file_name1)
    file_name2 = os.path.join(DATA_DIR, file_name2)
    file_name3 = os.path.join(DATA_DIR, file_name3)

    song_df.to_excel(file_name1) 
    new_song_df = song_df[["name", "artist","key", "liveness", "instrumentalness", "loudness", "mode", "speechiness", "tempo", "valence", "danceability", "energy", "acousticness"]].copy()
    new_song_df.to_excel(file_name2,index=False) 

    # Normalize features
    normfeat = ["key","loudness", "tempo"]
    normdf_minmax = new_song_df
    normdf_minmax = minmax_dfnorm(normdf_minmax, normfeat)
    
    normdf_minmax.to_excel(file_name3,index=False) 
 


        


