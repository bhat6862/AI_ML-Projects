'''Assignment (10/03/2026)
 Assignment Name : Spam Classifier Thinking 
 Description : Design a spam detection system: features, data needed, possible mistakes
'''



'''1. Features for Spam Detection
Features are the characteristics used by the system to identify spam messages.
Examples of features:
Presence of spam keywords (free, win, prize, offer)
Number of links in the message
Message length
Use of capital letters or special symbols
Sender email address or phone number
'''

'''2. Data Needed
To train a spam detection system, we need a dataset containing
Text messages or emails
Each message labeled as Spam or Not Spam (Ham)
Large number of examples for both spam and normal messages
Messages collected from emails, SMS, or social media

Example dataset:
Message	Label
"Win a free prize now!"	Spam
"Meeting at 4 PM tomorrow"	Not Spam
"Limited time offer click here"	Spam
"Please send the report today"	Not Spam'''

'''Possible Mistakes
A spam classifier can make two types of mistakes:

False Positive
A normal message is incorrectly classified as spam.

Example:
"Your bank OTP is 4567"
classified as spam.
False Negative
A spam message is classified as normal.
Example:
"Click here to claim your reward"
classified as normal.'''
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# Sample dataset
data = {
    "Message": [
        "Win a free iPhone now",
        "Meeting at 5 pm today",
        "Congratulations you won a prize",
        "Please submit the assignment",
        "Limited time offer click now",
        "Let's have lunch tomorrow"
    ],
    "Label": ["Spam", "Ham", "Spam", "Ham", "Spam", "Ham"]
}

# Create DataFrame
dataset = pd.DataFrame(data)

print("Dataset:")
print(dataset)

# Convert text to numeric features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(dataset["Message"])

# Labels
y = dataset["Label"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Test with new message
new_message = [""]
new_message_vector = vectorizer.transform(new_message)

prediction = model.predict(new_message_vector)

print("\nMessage:", new_message[0])
print("Prediction:", prediction[0])



'''This program demonstrates how a spam classifier works:

Collect spam and normal messages.

Convert text into numerical features.

Train a machine learning model.

Use the model to predict whether a new message is spam.'''