import joblib

model = joblib.load(
    "model/model.pkl"
)

skills = input("Enter skills: ")
probs = model.predict_proba([skills])[0]

classes = model.classes_

results = sorted(
    zip(classes, probs),
    key=lambda x: x[1],
    reverse=True
)

top3 = results[:3]

for role, score in top3:
    print(role, round(score * 100, 2), "%")

print("\nPredicted Role:")
print(top3[0][0])