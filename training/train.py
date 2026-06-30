import pandas as pd
import joblib
import os

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("Data/resumes.csv")

print(df)

X = df["skills"]
y = df["role"]

# Create model
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression())
])

# Train model
model.fit(X, y)

# Create model folder
os.makedirs("model", exist_ok=True)

# Save model
joblib.dump(
    model,
    "model/model.pkl"
)

print("✅ Model trained successfully!")