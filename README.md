# Schedule-based Harmonic Playlist Generation using Neural Networks

# RESEARCH PAPER AND PRESENTATION ARE AVAILABLE IN THE GIT REPOSITORY
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
 
You can pip instal this modules seperately from the windows command prompt or a linux terminal e.g
  ```sh
  $ pip install matplotlib
  ```
Our code was built in the anaconda python3 (in the base enviroment). The only module that anaoconda did not have was tensorflow
 
### Running Code
  - All the code is located in the folder named **code**
  - Run final_code_main.py in the windows command prompt, maC terminal or windows terminal
  - First go into the code directory
  ```sh
  $ cd code
  ```
  - Then execute the python file
  ```sh
  $ python final_project_main.py
  ```
  - After that follow the prompts
  - Below shows an example usage:
  ```sh
  (tf) C:\Users\roike\Documents\research\MachineDJ>python final_project_main.py
  2020-05-02 17:51:08.610787: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX AVX2

  *****************************     Hola Querida! *****************************
  Please input your schedule for the day. You have 4 activity options:
  (1) BeastMode, (2) Studying, (3) Beach Party, (4) Relaxing

  What is your activty  choice [1, 2, 3, 4], type q when done: 5
  Please input an activity out of these options: 1, 2, 3, or 4
  What is your activty  choice [1, 2, 3, 4], type q when done: 3
  How long will you be doing this activity in hrs: .5
  What is your activty  choice [1, 2, 3, 4], type q when done: 4
  How long will you be doing this activity in hrs: .4
  What is your activty  choice [1, 2, 3, 4], type q when done: 1
  How long will you be doing this activity in hrs: .2
  What is your activty  choice [1, 2, 3, 4], type q when done: 3
  How long will you be doing this activity in hrs: .1
  What is your activty  choice [1, 2, 3, 4], type q when done: q
  ... Exiting input stage
  ...We will start making your playlist
  ... YAY!! Your Schedule has been recieved  ...
  The schedule you created was this: [{'activity': 3, 'duration': 0.5}, {'activity': 4, 'duration': 0.4}, {'activity': 1, 'duration': 0.2}, {'activity': 3, 'duration': 0.1}]
```
  - To put in another schedule restart the program with Ctrl+C or by closing energy graph.

### NOTES
  - We stored an excel sheet with songs and features we exrtracted using the spotify API. All songs on your generated playlist will be pulled from that data set
  - Enter your schedule in the format of activity number and duration of tme in hours.
  - After you have input the time the machine learning algorithm will generate the playlist for you in form of an ordered list of songs
  - A graph of the energy flow the algorithm is emultes will also be displayed
