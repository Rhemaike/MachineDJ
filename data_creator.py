# Author: Rhema Ike

import pandas as pd
import os

from song_import import minmax_dfnorm


# Creation of Energy Boost Songs

dir_name = "DataSets"

filename = "Song_Feature_Data_set_less.xlsx"  #input file
filename = "test.xlsx"
filename = os.path.join(dir_name, filename)
df = pd.read_excel(filename)
song_num = df.shape[0]
dir_name = "TestSets"
print("Songs in file {}: {}".format(filename, song_num) )
y_list = [0] * pow(song_num, 2)
y_df = pd.DataFrame(y_list, columns=["y"], dtype="int32")

rng = pow(song_num, 2)
data = [0] * rng
str_data = [""]*rng
x_dic = {"key1": data, "mode1": data, "tempo1": data, "key2": data, "mode2": data, "tempo2": data}
mix_dic = {"name1":str_data, "artist1":str_data, "key1":data, "mode1": data, "tempo1": data, "name2":str_data, "artist2":str_data, "key2": data, "mode2": data, "tempo2": data, "y":y_list}

mix_df = pd.DataFrame(mix_dic, columns=["name1","artist1","key1","mode1","tempo1","name2","artist2","key2","mode2","tempo2","y"])
x_df = pd.DataFrame(x_dic,columns=["key1","mode1","tempo1","key2","mode2","tempo2"])
max_song_key = 11
min_song_key = 0
row_count = 0

tempo_lim = 0.04  # 4 percent
for _, row in df.iterrows():
    song1_key = int(row["key"])
    song1_mode = int(row["mode"])
    song1_tempo = int(row["tempo"])
    song1_artist = row["artist"]
    song1_name = row["name"]
    tempo_high_bound = song1_tempo + (song1_tempo * tempo_lim)
    tempo_low_bound = song1_tempo - (song1_tempo * tempo_lim/2)
    for _, row2 in df.iterrows():
        song2_key = int(row2["key"])
        song2_mode = int(row2["mode"])
        song2_tempo = int(row2["tempo"])
        song2_name = row2["name"]
        song2_artist = row2["artist"]

        # Inputing data in new data set
        mix_df["key1"][row_count] = song1_key
        mix_df["mode1"][row_count] = song1_mode
        mix_df["tempo1"][row_count] = song1_tempo
        mix_df["name1"][row_count] = song1_name
        mix_df["artist1"][row_count] = song1_artist
        mix_df["key2"][row_count] = song2_key
        mix_df["mode2"][row_count] = song2_mode
        mix_df["tempo2"][row_count] = song2_tempo
        mix_df["name2"][row_count] = song2_name
        mix_df["artist2"][row_count] = song2_artist

        if song2_tempo > tempo_low_bound and song2_tempo < tempo_high_bound:
            if song1_mode == 0:
                if song1_key == song2_key and song1_mode != song2_mode:
                    mix_df["y"][row_count] = 1 
                elif song2_key == (song1_key + 1) and song1_mode == song2_mode:
                    mix_df["y"][row_count] = 1 
                elif song1_key == max_song_key and song2_key == min_song_key and song1_mode == song2_mode:
                    mix_df["y"][row_count] = 1 
                else:
                    mix_df["y"][row_count] = 0
            if song1_mode == 1:
                if song2_key == (song1_key + 1) and song1_mode == song2_mode:
                    mix_df["y"][row_count] = 1 
                elif song1_key == max_song_key and song2_key == min_song_key and song1_mode == song2_mode:
                    mix_df["y"][row_count] = 1 
                else:
                    mix_df["y"][row_count] = 0
        else:
            mix_df["y"][row_count] = 0 

        
        if(row_count % 100 == 0):
            prog = ((row_count + 1)/ rng) * 100
            print("### progress: {:.2f} % ({}/{})".format(prog, row_count+1, rng))
        row_count += 1

outx_file = "energy_boost_x.xlsx"
outy_file = "energy_boost_y.xlsx"
mix_file = "energy_boost_mix.xlsx"

outx_file = os.path.join(dir_name, outx_file)
outy_file = os.path.join(dir_name, outy_file)
mix_file = os.path.join(dir_name, mix_file)

mix_df.to_excel(mix_file,index=False) 

x_df = mix_df[["key1","mode1","tempo1", "key2","mode2","tempo2"]].copy()
y_df = mix_df[["y"]].copy()

y_true_values = len(y_df[y_df["y"] == 1].index)
print("Percentage of ones = {}, ({}/{})".format((y_true_values/rng), y_true_values, rng))

# Normalise The tempo 
normfeat = ["tempo1","tempo2"]
x_df = minmax_dfnorm(x_df, normfeat)

no_hot_file = "energy_boost_x_no_one_hot.xlsx"
no_hot_file = os.path.join(dir_name,no_hot_file)
x_df.to_excel(no_hot_file,index=False)


# changed encoding of the key
key1_list = []
key2_list = []

zeros = [0] * rng
key1_dic = {}
key2_dic = {}
num_of_keys = 12
for x in range(num_of_keys):
    key_name = "key1" + str(x + 1)
    key1_list.append(key_name)
    key1_dic[key_name] = zeros

for x in range(num_of_keys):
    key_name = "key2" + str(x + 1)
    key2_list.append(key_name)
    key2_dic[key_name] = zeros

key_df1 = pd.DataFrame(key1_dic)
key_df2 = pd.DataFrame(key2_dic)

print("key1 list", key1_list)
print("key2 list", key2_list)

for index,row in x_df.iterrows():
    key = int(row["key1"])
    temp_list = [0] * num_of_keys
    temp_list[key] = 1
    key_df1.iloc[index] = temp_list

    key = int(row["key2"])
    temp_list = [0] * num_of_keys
    temp_list[key] = 1
    key_df2.iloc[index] = temp_list

x_first_df = x_df[["mode1","tempo1"]].copy()
x_second_df = x_df[["mode2","tempo2"]].copy()

x_df = pd.concat([x_first_df, key_df1, x_second_df, key_df2], axis=1)

x_df.to_excel(outx_file,index=False)
y_df.to_excel(outy_file,index=False) 





