'''Assignment (24/03/2026) 
Assignment Name :Word Importance Explorer 
Description : Use TF-IDF on 5 documents and identify top keywords with explanation.'''

from sklearn.feature_extraction.text import TfidfVectorizer

# Step 1: Documents
documents = [
    "Machine learning is used for data analysis and prediction",
    "Artificial intelligence and machine learning are transforming industries",
    "Data science involves statistics data analysis and machine learning",
    "Deep learning is a subset of machine learning",
    "AI is widely used in healthcare and finance"
]

# Step 2: TF-IDF with stopwords removal (IMPORTANT)
vectorizer = TfidfVectorizer(stop_words='english')

X = vectorizer.fit_transform(documents)

# Step 3: Get feature names
features = vectorizer.get_feature_names_out()

# Step 4: Display top 5 keywords for each document
for i, doc in enumerate(X):
    print(f"\nDocument {i+1}:")
    
    scores = list(zip(features, doc.toarray()[0]))
    
    # Sort words based on TF-IDF score
    sorted_words = sorted(scores, key=lambda x: x[1], reverse=True)
    
    # Print top 5 keywords
    for word, score in sorted_words[:5]:
        if score > 0:
            print(word, ":", round(score, 2))

#OUTPUT:
'''
Document 1:
prediction : 0.53
analysis : 0.43
data : 0.43
used : 0.43
learning : 0.3

Document 2:
artificial : 0.46
industries : 0.46
intelligence : 0.46
transforming : 0.46
learning : 0.26

Document 3:
data : 0.61
involves : 0.38
science : 0.38
statistics : 0.38
analysis : 0.31

Document 4:
learning : 0.59
deep : 0.53
subset : 0.53
machine : 0.3

Document 5:
ai : 0.46
finance : 0.46
healthcare : 0.46
widely : 0.46
used : 0.37

Document 1
prediction, analysis, data, used
Shows focus on data analysis and prediction
Document 2
artificial, intelligence, industries, transforming
Clearly represents Artificial Intelligence domain
Document 3
data, science, statistics, analysis
Related to Data Science concepts
Document 4
deep, learning, subset
Represents Deep Learning topic
Document 5
ai, healthcare, finance
Shows AI applications in real-world fields'''