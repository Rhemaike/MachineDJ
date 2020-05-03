# author: Rhema Ike

# Imports
import pandas as pd
from removequote import removequote

class Song:
    def __init__(self, file_name):
        self.df = pd.read_excel(file_name)
        self.df["Song"] = self.df["Song"].apply(removequote)
        self.columns = self.df.columns.tolist()
        # self.printdf()
        self.songnames = []

        self.itter()

    def printdf(self):
        print(self.df)
        print(self.columns)

    def itter(self):
        count = 0
        # for header in self.columns:
        #     print(header, "             ", end='')
        # print()
        for _, rows in self.df.iterrows():
            # for header in self.columns:
            #     print(rows[header], "    ", end = '')
            # print()
            self.songnames.append(rows["Song"])
            count += 1
            if count == 50:
                break

        # print(self.songnames)

    def get_names(self):
        return self.songnames
       
if __name__ == "__main__":
    file_name = "Billboard_songs_2010-19.xlsx"
    s = Song(file_name)

    songdf = pd.DataFrame(columns=["song_title", "tempo", "key", "Genre"])
    info = {"song_title":"Shakeit out",
            "tempo":"h",
            "key":3,
            "Genre":4
            }
    songdf = songdf.append(info,ignore_index=True)
    songdf = songdf.append(info,ignore_index=True)
    print(songdf)
    s.itter()
