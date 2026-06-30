import pandas as pd
import joblib

from sklearn.metrics import classification_report

from sklearn.model_selection import train_test_split

df = pd.read_csv("data/resumes.csv")

X = df["skills"]
y = df["role"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = joblib.load(
    "models/model.pkl"
)

predictions = model.predict(X_test)

print(
    classification_report(
        y_test,
        predictions
    )
)