from fastapi import FastAPI
from pydantic import BaseModel
import json
from model.model import predict_pipeline
from model.model import __version__ as model_version

app = FastAPI()


class Info(BaseModel):
    id : list
    camName : str


@app.get("/")
def home():
    return "Hello"


@app.post("/getPred")
def getInformation(info : Info):
    id = info.id
    print(id)
    prediction = predict_pipeline(id)
    return {
        "pred" : prediction
    }