'''Assignment Name : NLP Mini App 
Description : fake news detecto'''

import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Get current file location
base_path = os.path.dirname(__file__)

# Correct path to CSV
file_path = os.path.join(base_path, "news.csv")

# Load dataset
df = pd.read_csv(file_path)

X = df['text']
y = df['label']

vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vec, y)

news = input("Enter news: ")
news_vec = vectorizer.transform([news])

prediction = model.predict(news_vec)

if prediction[0] == 1:
    print("REAL NEWS")
else:
    print("FAKE NEWS")