# SI507_final_project
A README containing any special instructions for running your code (e.g., how to supply API
keys) as well as a brief description of how to interact with your program.
README describing your Data Structure (graphs or trees)

## REQUIRED PYTHON PACKAGES:
* spotipy
* requests
* bs4
* pandas
* seaborn
* scikit-learn
* graphviz
* IPython
* PIL

## SUPPLYING API KEY FOR SPOTIFY DATA
The Spotify API has been used to retrieve information about different songs spread over multiple decades. It contains various features of songs like valence, tempo, key, etc. The output is in JSON format.

To access the data from the Spotify API, authentication is required. The access token was obtained by registering an application on the Spotify Developer Dashboard and following the authentication process

You will receive a client id and a client_secret key.

This key will be pasted in the
'clientid, clientsecret = ' 
line in the 'data_to_json_final.ipynb' file for accessing the Spotify API.

## DATA STRUCTURE
A decision tree was made by selecting features of songs that have the highest correlation with popularity and splitting nodes based on these correlations.

This was done using the machine learning Decision Tree Classifier.

## INTERACTING WITH THE PROGRAM
* To interact with the program, first make sure you have the merged file of the Spotify and Billboard data (‘merged_data.json’ file has been uploaded to Github repo). If you want to obtain the data yourself, first run the cells in the 'data_to_json_final.ipynb' file after putting in the Spotify client id and the client_secret. Then run the 'putting_data_together_final.py' file to obtain the ‘merged_data.json’ file.(Make changes in file path wherever necessary)
* Run the ‘tree_visualizations_final.py’ file. Make necessary changes in the path for accessing the ‘merged_data.json’ file. Also, make any changes in the code wherever you would like to change the path of the images getting saved. Running this file will create all trees and visualizations needed for the main interactive program to run.
* Now run the ‘final_run.py’ file and answer the prompts to obtain visualizations as desired. (Make changes in file path wherever necessary)
* The program will first display a welcome message and then proceed with displaying options for the user to choose from.
