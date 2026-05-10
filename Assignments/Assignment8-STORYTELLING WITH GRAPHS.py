'''Assignment (28/02/2026) 
Assignment Name : Storytelling with Graphs
 Description : Create bar chart, pie chart, histogram and write a short data story explaining trends.'''


import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv(r"C:\Users\akshi\OneDrive\Desktop\AIML INTERNSHIP ASSIGNMENTS\Assignment8-sTORY TELLING WITH GRAPH\Student Attitude and Behavior.csv")

# 1️⃣ Bar Chart – Department Distribution
dept_counts = data['Department'].value_counts()

plt.figure()
dept_counts.plot(kind='bar')
plt.title("Number of Students by Department")
plt.xlabel("Department")
plt.ylabel("Number of Students")
plt.show()

# 2️⃣ Pie Chart – Gender Distribution
gender_counts = data['Gender'].value_counts()

plt.figure()
gender_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title("Gender Distribution")
plt.ylabel("")
plt.show()

# 3️⃣ Histogram – College Marks Distribution
plt.figure()
plt.hist(data['college mark'], bins=10)
plt.title("Distribution of College Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()


'''Data Story (Trends):

The bar chart shows the number of students in each department, helping identify which department has the highest student participation.
The pie chart represents the gender distribution in the dataset, showing the percentage of male and female students.
The histogram of college marks shows how marks are distributed and helps identify the most common score range among students.
From the graphs, we can observe that most students fall within a moderate to high marks range, indicating good academic performance.
Overall, the visualizations help understand student demographics and academic trends, making the data easier to interpret.'''