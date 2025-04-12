from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import joblib

app = FastAPI()

# Load SentenceTransformer and classifier
clf = joblib.load("model/Intent Classifier.pkl")
model = SentenceTransformer('sentence-transformers/distiluse-base-multilingual-cased-v2')

class TextRequest(BaseModel):
    text: str

@app.post("/predict")
def predict(req: TextRequest):
    embedding = model.encode([req.text])
    pred = clf.predict(embedding)
    return {"intent": pred[0]}