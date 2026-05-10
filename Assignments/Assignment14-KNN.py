#Assignment (07/03/2026)
#Assignment Name: KNN in Real Life
'''1. Explanation: Netflix-like Recommendations using KNN
KNN (K-Nearest Neighbors) is a machine learning algorithm that finds similar items or users based on their features. In recommendation systems like Netflix, KNN can be used to suggest movies by comparing users’ preferences.
For example, Netflix stores information such as:
Movies watched
Movie rating
Genres liked by users
If two users have similar watching patterns, they are considered neighbors. The system recommends movies that similar users have watched but the current user has not.

Example:
User A likes Action, Sci-Fi, Thriller
User B likes Action, Sci-Fi
Since their interests are similar, Netflix may recommend the movies watched by User A to User B.
Thus, KNN helps in finding similar users or movies and recommending content accordingly.'''
'''2. Small Similarity Example
User	Action	Comedy	Drama
User1	  5	     1	     2
User2	  4	     1	     1
User3	  1	     5	     4

User1 and User2 have similar ratings for Action movies, so they are nearest neighbors.
If User1 watched a movie that User2 has not seen, the system may recommend that movie to User2.'''

from sklearn.neighbors import NearestNeighbors
import numpy as np

# Example user preference data
# Columns: Action, Comedy, Drama
data = np.array([
    [5, 1, 2],   # User1
    [4, 1, 1],   # User2
    [1, 5, 4]    # User3
])

# Train KNN model
model = NearestNeighbors(n_neighbors=2, metric='euclidean')
model.fit(data)

# Find similar users for User1
distances, indices = model.kneighbors([data[0]])

print("Nearest neighbors for User1:", indices)

#Nearest neighbors for User1: [[0 1]]
# This means User2 is most similar to User1, so recommendations can be made based on User2’s preferences.