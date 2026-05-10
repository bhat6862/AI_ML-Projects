'''Assignment (26/03/2026) 
Assignment Name : Movie Review Analyzer 
Description : Build a simple sentiment analyzer and test on 5 reviews.'''
# Install if needed
#RUNNED IN GOOGLE COLAB OR JUPYTER NOTEBOOK   
# pip install textblob

from textblob import TextBlob

# Step 1: Reviews
reviews = [
    "The movie was amazing and I loved it",
    "It was a terrible movie, very boring",
    "The acting was good but the story was average",
    "Absolutely fantastic experience, great visuals",
    "Worst movie ever, waste of time"
]

# Step 2: Analyze sentiment
for review in reviews:
    analysis = TextBlob(review)
    polarity = analysis.sentiment.polarity
    
    # Step 3: Classify
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    print("Review:", review)
    print("Sentiment:", sentiment)
    print("Polarity:", round(polarity, 2))
    print("-" * 40)


#OUTPUT:
'''Review: The movie was amazing and I loved it
Sentiment: Positive
Polarity: 0.65
----------------------------------------
Review: It was a terrible movie, very boring
Sentiment: Negative
Polarity: -1.0
----------------------------------------
Review: The acting was good but the story was average
Sentiment: Positive
Polarity: 0.18
----------------------------------------
Review: Absolutely fantastic experience, great visuals
Sentiment: Positive
Polarity: 0.6
----------------------------------------
Review: Worst movie ever, waste of time
Sentiment: Negative
Polarity: -0.6
----------------------------------------
'''