import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
from utils.preprocess import clean_text

# Load dataset
df = pd.read_csv('data/dummy.csv')


# Clean text
df['cleaned'] = df['Complaint'].apply(clean_text)

# Split data
X_train, X_test, y_train, y_test = train_test_split(df['cleaned'], df['Team'], test_size=0.2, random_state=42)

# Build pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression())
])

# Train the model
pipeline.fit(X_train, y_train)

# Evaluate
y_pred = pipeline.predict(X_test)
print("📊 Classification Report:\n")
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(pipeline, 'models/classifier.pkl')
print("✅ Model saved to models/classifier.pkl")