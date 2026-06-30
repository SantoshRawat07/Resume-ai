from fastapi import FastAPI

from pydantic import BaseModel

import joblib

app = FastAPI()

model = joblib.load(
    "model/model.pkl"
)

class ResumeRequest(BaseModel):
    skills: str

@app.post("/predict")
def predict(data: ResumeRequest):

    result = model.predict(
        [data.skills]
    )[0]

    return {
        "predicted_role": result
    }