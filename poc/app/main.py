
from fastapi import FastAPI
from keras.models import load_model
from util.calc_descriptor import calc_descriptor
from keras.models import Sequential

app = FastAPI()

model: Sequential = load_model("model")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/predict/{smile}")
def predict(smile: str) -> float:
    features = calc_descriptor(smile)
    pred = model.predict(features)
    return float(pred[0][0])