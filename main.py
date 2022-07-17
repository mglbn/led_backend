from fastapi import FastAPI
from mystrip import MyStrip
from pydantic import BaseModel

class MyModel(BaseModel):
    effect : str

app = FastAPI()
strip = MyStrip()

effects = {
    "rot" : strip.rot,
    "blau": strip.blau,
    "ausschalten": strip.aus
}





@app.post("/")
def root(model : MyModel):
    return model



