'''ssignment:Assignment (26/02/2026) 
Assignment Name : Data Doctor 
Description : Clean a dataset by handling missing values, removing duplicates, standardizing text, and explain why cleaning matters.'''


import pandas as pd

# Load dataset
data = pd.read_csv(r"C:\Users\akshi\OneDrive\Desktop\AIML INTERNSHIP ASSIGNMENTS\Assignment11-DATA DOCTOR\studentdataset.csv.csv")

# 1. Check missing values
print("Missing Values Before Cleaning:")
print(data.isnull().sum())

# 2. Handle missing values
# Fill numeric columns with mean
numeric_cols = data.select_dtypes(include=['int64','float64']).columns
data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())

# Fill text columns with 'Unknown'
text_cols = data.select_dtypes(include=['object']).columns
data[text_cols] = data[text_cols].fillna("Unknown")

# 3. Remove duplicate rows
data = data.drop_duplicates()

# 4. Standardize text (convert text to lowercase)
for col in text_cols:
    data[col] = data[col].str.lower()

# Display cleaned dataset
print("\nCleaned Dataset (Top Rows):")
print(data.head())

# Check missing values after cleaning
print("\nMissing Values After Cleaning:")
print(data.isnull().sum())


'''Why Data Cleaning Matters:-

It removes missing or incorrect data, improving data quality.

It eliminates duplicate records, preventing biased results.

Standardizing text ensures consistency across the dataset.

Clean data improves the accuracy of analysis and machine learning models.

It makes the dataset reliable and ready for further processing.'''