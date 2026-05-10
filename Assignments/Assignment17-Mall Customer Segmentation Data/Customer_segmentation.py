'''Assignment (18/03/2026) 
Assignment Name : Customer Segmentation 
Description : Perform K-Means clustering on a mall dataset and describe customer groups.'''
# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Step 2: Load dataset
# Make sure Mall_Customers.csv is in same folder
df = pd.read_csv(r"C:\Users\akshi\OneDrive\Desktop\AIML INTERNSHIP ASSIGNMENTS\Assignment17-Mall Customer Segmentation Data\Mall_Customers.csv")

# Step 3: Select features (important)
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# Step 4: Use Elbow Method to find optimal clusters
wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# Plot Elbow Graph
plt.figure()
plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# Step 5: Apply K-Means (usually K = 5)
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
y_kmeans = kmeans.fit_predict(X)

# Step 6: Visualize clusters
plt.figure()
plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=y_kmeans)
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.title('Customer Segments')
plt.show()