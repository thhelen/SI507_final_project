import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_validate, train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import graphviz
from IPython.display import Image
import numpy as np


with open('C:/Users/thhelen/Desktop/si507_lec/hw/Final_Project/merged_data.json', 'r') as chache_file:
    cache_spotify = json.load(chache_file)
merged_data= pd.DataFrame(cache_spotify)
# creating a cloumn for popular song or not based on popularity from spotify API
is_popular_spotify = lambda x: 1 if x > 50 else 0
merged_data['is_popular_spotify'] = merged_data['track_pop_spotify'].apply(is_popular_spotify)

# creating a cloumn for popular song or not based on popularity from Billboard data
is_popular_BB = lambda x: 1 if x > 50 else 0
merged_data['is_popular_BB'] = merged_data['rank_billboard'].apply(is_popular_BB)

X = merged_data.drop(['track_name','type', 'id', 'uri', 'track_href', 'analysis_url','artist', 'album'], axis=1)

# FIRST VISUALIZATION

correlation_heatmap = sns.heatmap(X.corr(), cmap='coolwarm')
plt.savefig('correlation_heatmap.png')
plt.show()

# SECOND VISUALIZATION
## POPULARITY - TREE - BASED ON SPOTIFY POPULARITY DATA
X = merged_data.drop(columns=['type', 'id', 'uri', 'track_href', 'analysis_url','track_name', 'artist', 'album', 'track_pop_spotify','is_popular_spotify','is_popular_BB','rank_billboard'])
y = merged_data["is_popular_spotify"]

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=42)
def cross_validate_return(X_train, y_train, depth):
    model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    scores = cross_validate(model, X_train, y_train, 
                        return_train_score=True, cv=10)
    return_df = pd.DataFrame(pd.DataFrame(scores).mean()).iloc[2:].T
    return [round(return_df.train_score[0], 3),
            round(return_df.test_score[0],3), depth]
data = []
i = 1
while i < 20:
    data.append(cross_validate_return(X_train, y_train, i))
    i += 1
df = pd.DataFrame(data, columns=['train_score', 'validation_score',
                  'max_depth'])
optimal_depth = df.max_depth[df.validation_score.argmax()]
print(f"The optimal depth is: {optimal_depth}")
optimal_model = DecisionTreeClassifier(max_depth=optimal_depth)
optimal_model.fit(X_train, y_train)
def display_tree(feature_names, tree, counts=False):
    """For binary classification only"""
    dot = export_graphviz(
        tree,
        out_file=None,
        feature_names=feature_names,
        class_names=tree.classes_.astype(str),
        impurity=False,
    )
    return graphviz.Source(dot)
g = display_tree(X_train.columns, optimal_model) 
g.render("optimal_spotify", format="png")

for depth in [1, 3, 4, 5, 6, 7, 8, 9, 10]:
    model = DecisionTreeClassifier(max_depth=depth)
    model.fit(X_train, y_train)    
    g = display_tree(X_train.columns, model) 
    g.render(f'tree_spotify_{depth}', format="png")


## POPULARITY - TREE - BASED ON BILLBOARD POPULARITY DATA
X = merged_data.drop(columns=['type', 'id', 'uri', 'track_href', 'analysis_url','track_name', 'artist', 'album', 'track_pop_spotify','is_popular_spotify','is_popular_BB','rank_billboard'])
y = merged_data["is_popular_BB"]

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=42)
def cross_validate_return(X_train, y_train, depth):
    model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    scores = cross_validate(model, X_train, y_train, 
                        return_train_score=True, cv=10)
    return_df = pd.DataFrame(pd.DataFrame(scores).mean()).iloc[2:].T
    return [round(return_df.train_score[0], 3),
            round(return_df.test_score[0],3), depth]
data = []
i = 1
while i < 20:
    data.append(cross_validate_return(X_train, y_train, i))
    i += 1
df = pd.DataFrame(data, columns=['train_score', 'validation_score', 'max_depth'])
optimal_depth = df.max_depth[df.validation_score.argmax()]
print(f"The optimal depth is: {optimal_depth}")
optimal_model = DecisionTreeClassifier(max_depth=optimal_depth)
optimal_model.fit(X_train, y_train)
g = display_tree(X_train.columns, optimal_model) 
g.render("optimal_BB", format="png")
for depth in [1, 2, 3, 5, 6, 7, 8, 9, 10]:
    model = DecisionTreeClassifier(max_depth=depth)
    model.fit(X_train, y_train)    
    g = display_tree(X_train.columns, model) 
    g.render(f'tree_BB_{depth}', format="png")

# THIRD VISUALIZATION 
## Analyze which tempo has higher popularity over a period of time.

tempo_groups = pd.cut(merged_data['tempo'], bins=[0, 60, 80, 100, 120, 150, 180, 220], labels=['<60', '60-80', '80-100', '100-120', '120-150', '150-180', '180+'])
grouped_df = merged_data.groupby([tempo_groups, 'decade'])['track_pop_spotify'].mean().reset_index()
sns.heatmap(grouped_df.pivot_table(index='decade', columns='tempo', values='track_pop_spotify'), cmap='coolwarm', annot=True, fmt='.0f')
plt.title("Popularity")
plt.savefig('tempo_vs_popularity.png')
plt.show()

## Analyze which valence has higher popularity over a period of time.

valence_groups = pd.cut(merged_data['valence'], bins=[0, 0.2, 0.4, 0.6, 0.8, 1], labels=['<0.2', '0.2-0.4', '0.4-0.6', '0.6-0.8', '0.8+'])
grouped_df = merged_data.groupby([valence_groups, 'decade'])['track_pop_spotify'].mean().reset_index()
sns.heatmap(grouped_df.pivot_table(index='decade', columns='valence', values='track_pop_spotify'), cmap='coolwarm', annot=True, fmt='.0f')
plt.title("Popularity")
plt.savefig('valence_vs_popularity.png')
plt.show()

## Analyze which energy has higher popularity over a period of time.

energy_groups = pd.cut(merged_data['energy'], bins=[0, 0.2, 0.4, 0.6, 0.8, 1], labels=['<0.2', '0.2-0.4', '0.4-0.6', '0.6-0.8', '0.8+'])
grouped_df = merged_data.groupby([energy_groups, 'decade'])['track_pop_spotify'].mean().reset_index()
sns.heatmap(grouped_df.pivot_table(index='decade', columns='energy', values='track_pop_spotify'), cmap='coolwarm', annot=True, fmt='.0f')
plt.title("Popularity")
plt.savefig('energy_vs_popularity.png')
plt.show()

## Analyze which acousticness has higher popularity over a period of time.

acousticness_groups = pd.cut(merged_data['acousticness'], bins=[0, 0.2, 0.4, 0.6, 0.8, 1], labels=['<0.2', '0.2-0.4', '0.4-0.6', '0.6-0.8', '0.8+'])
grouped_df = merged_data.groupby([acousticness_groups, 'decade'])['track_pop_spotify'].mean().reset_index()
sns.heatmap(grouped_df.pivot_table(index='decade', columns='acousticness', values='track_pop_spotify'), cmap='coolwarm', annot=True, fmt='.0f')
plt.title("Popularity")
plt.savefig('acousticness_vs_popularity.png')
plt.show()

## Analyze which danceability has higher popularity over a period of time.

danceability_groups = pd.cut(merged_data['danceability'], bins=[0, 0.2, 0.4, 0.6, 0.8, 1], labels=['<0.2', '0.2-0.4', '0.4-0.6', '0.6-0.8', '0.8+'])
grouped_df = merged_data.groupby([danceability_groups, 'decade'])['track_pop_spotify'].mean().reset_index()
sns.heatmap(grouped_df.pivot_table(index='decade', columns='danceability', values='track_pop_spotify'), cmap='coolwarm', annot=True, fmt='.0f')
plt.title("Popularity")
plt.savefig('danceability_vs_popularity.png')
plt.show()