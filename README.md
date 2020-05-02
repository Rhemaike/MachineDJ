# Schedule-based Harmonic Playlist Generation usingNeural Networks

[![Build Status](https://github.com/Rhemaike/MachineDJ)](https://github.com/Rhemaike/MachineDJ)

We have build a software that allows users to create playlist for their entire day based on their schedule. This is a proof of concept so the amount of activities a user can have in their schedule is limited to 4:

 - BeastMode (1)
 - Studying (2)
 - BeachParty (3)
 - Relaxing (4)
 
Our code base contains jupyter notebooks for training the four neuralnetworks used in our system, pretrained models, all the data set we used and Python code to get song data from spotify using the spotify python api and the main pipe lne code called final_project_main.py. 

# HOW TO RUN CODE 

### Dependencies
 - tensorflow
 - numpy
 - pandas
 - scikit-learn
 - matplotlib
 
You can pip instal this modules seperately e.g
  ```sh
  $ pip install matplotlib
  ```
Our code was built in the anaconda python3 (in the base enviroment). The only module that anaoconda did not have was tensorflow
 
### Running Code
  - Run final_code_main.py
  ```sh
  $ python final_project_main.py
  ```
  - After that follow the prompts
  - We stored an excel sheet with songs and features we exrtracted using the spotify API. All songs on your generated playlist will be pulled from that data set
  - Enter your schedule in the format of activity number and duration of tme in hours.
  - After you have input the time the machine learning algorithm will generate the playlist for you in form of an ordered list of songs
  - A graph of the energy flow the algorithm is emultes will also be displayed
  - To put in another schedule restart the program with Ctrl+C or closing energy graph.