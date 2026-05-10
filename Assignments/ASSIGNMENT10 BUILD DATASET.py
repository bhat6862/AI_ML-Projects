'''Assignment (03/03/2026)
Assignment Name : Build Your First Dataset
Description : Create a dataset (e.g., study hours vs marks), identify features & labels, predict relationship.
'''
import pandas as pd
from sklearn.linear_model import LinearRegression

# Create dataset
data = {
    "Study Hours": [2, 3, 4, 5, 6, 7, 8],
    "Marks": [45, 50, 60, 70, 80, 85, 90]
}

dataset = pd.DataFrame(data)

print("Dataset")
print(dataset)

# Identify features and labels
X = dataset[["Study Hours"]]   # Feature
y = dataset["Marks"]           # Label

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict marks for 9 study hours
predicted_marks = model.predict([[9]])

print("\nPredicted Marks for 9 study hours:", predicted_marks[0])

'''
OUTPUT:-
Dataset
   Study Hours  Marks
0            2     45
1            3     50
2            4     60
3            5     70
4            6     80
5            7     85
6            8     90

Predicted Marks for 9 study hours: 100.71428571428572'''


'''

Features and Labels
Feature (Input): Study Hours
Label (Output): Marks

In machine learning, features are the input variables, and labels are the values we want to predict.

Relationship Prediction
From the dataset, we can observe that as study hours increase, marks also increase.
This shows a positive relationship between study time and exam performance.

For example:
A student studying 2 hours scored 45 marks.
A student studying 8 hours scored 90 marks.
This means that more study hours generally lead to higher marks, which can be predicted using machine learning models like Linear Regression.'''
