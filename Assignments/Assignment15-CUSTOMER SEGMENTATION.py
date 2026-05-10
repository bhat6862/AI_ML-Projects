'''Assignment (11/03/2026)
Assignment Name : Customer Segmentation
Description : Perform K-Means clustering on a mall dataset and describe customer groups.'''

import pandas as pd
from sklearn.cluster import KMeans

# Sample mall dataset
data = {
    "CustomerID": [1,2,3,4,5,6,7,8,9,10],
    "Annual Income": [15,16,17,18,19,70,72,74,76,78],
    "Spending Score": [39,81,6,77,40,6,94,3,72,10]
}

dataset = pd.DataFrame(data)

print("Mall Customer Dataset:")
print(dataset)

# Select features for clustering
X = dataset[["Annual Income","Spending Score"]]

# Apply K-Means
kmeans = KMeans(n_clusters=3)
dataset["Cluster"] = kmeans.fit_predict(X)

print("\nClustered Customers:")
print(dataset)


'''output:
Mall Customer Dataset:
   CustomerID  Annual Income  Spending Score
0           1             15              39
1           2             16              81
2           3             17               6
3           4             18              77
4           5             19              40
5           6             70               6
6           7             72              94
7           8             74               3
8           9             76              72
9          10             78              10

Clustered Customers:
   CustomerID  Annual Income  Spending Score  Cluster
0           1             15              39        2
1           2             16              81        1
2           3             17               6        2
3           4             18              77        1
4           5             19              40        2
5           6             70               6        0
6           7             72              94        1
7           8             74               3        0
8           9             76              72        1
9          10             78              10        0
[10 rows x 4 columns]
'''