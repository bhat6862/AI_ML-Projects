'''Assignment (24/02/2026)
Assignment Name : Dataset Detective
Description : Load a dataset, display top rows, find highest value column, count missing values, share 5 insights.'''
import pandas as pd

# Load the dataset
data = pd.read_csv("C:\\Users\\akshi\\OneDrive\\Desktop\\AIML INTERNSHIP ASSIGNMENTS\\Assignment7\\Student Attitude and Behavior.csv")

# Display top 5 rows
print("Top 5 Rows of Dataset")
print(data.head())

# Find highest values in numeric columns
print("\nHighest Values in Numeric Columns")
print(data[['Height(CM)', 'Weight(KG)', '10th Mark', '12th Mark', 'college mark']].max())

# Count missing values
print("\nMissing Values in Each Column")
print(data.isnull().sum())


#Insights:-
#1.The dataset contains 19 columns related to student behavior, academics, and lifestyle, such as marks, hobbies, stress level, and social media usage.
#2The highest academic score in college marks is 100, while the highest 10th mark is 98 and 12th mark is 94, showing strong academic performance among some students.
#3The maximum height recorded is 192 cm and maximum weight is 106 kg, indicating a wide range of physical attributes among students.
#4.There are no missing values in the dataset, meaning the dataset is clean and suitable for analysis without additional preprocessing.
#5The dataset includes behavioral and lifestyle factors such as study time, stress level, travelling time, and part-time jobs, which can be used to analyze how these factors influence student academic performance.