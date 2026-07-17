import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("spam.csv")

# Features and Labels
X = data["Message"]
y = data["Label"]

# Convert text to numbers
vectorizer = CountVectorizer()
X_vector = vectorizer.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_vector, y, test_size=0.3, random_state=42
)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Prediction
prediction = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, prediction))

# Test custom message
message = ["Congratulations! You won a free iPhone."]
message_vector = vectorizer.transform(message)

result = model.predict(message_vector)

print("Message:", message[0])
print("Prediction:", result[0])