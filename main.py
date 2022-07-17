from fastapi import FastAPI
from mystrip import MyStrip
from pydantic import BaseModel
from rpi_ws281x import *

class MyModel(BaseModel):
    effekt : str

app = FastAPI()
strip = MyStrip()

effects = {
    "rot" : strip.rot,
    "blau": strip.blau,
    "ausschalten": strip.aus
}





@app.post("/")
def root(model : MyModel):
    return {"ok":True}



