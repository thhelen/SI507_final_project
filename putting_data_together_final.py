import pandas as pd
import json
with open('C:/Users/thhelen/Desktop/si507_lec/hw/Final_Project/cache_billboard.json', 'r') as chache_file:
    cache_billboard = json.load(chache_file)
billboard_df= pd.DataFrame(cache_billboard)
with open('C:/Users/thhelen/Desktop/si507_lec/hw/Final_Project/cache_spotify.json', 'r') as chache_file:
    cache_spotify = json.load(chache_file)
spotify_df= pd.DataFrame(cache_spotify)
spotify_df['track_name'] = spotify_df['track_name'].str.title().str.strip()
billboard_df['title'] = billboard_df['title'].str.title().str.strip()
billboard_df = billboard_df.rename(columns={'title': 'track_name','rank': 'rank_billboard'})
billboard_df = billboard_df.drop(columns=['year', 'artists'])
merged_df = pd.merge(spotify_df, billboard_df, on='track_name', how='inner')
merged_df=pd.DataFrame(merged_df)
merged_df['rank_billboard'] = merged_df['rank_billboard'].astype(int)
#insert file path here
merged_df.to_json('C:/Users/thhelen/Desktop/si507_lec/hw/Final_Project/merged_data.json', orient='records')