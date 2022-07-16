from fastapi import FastAPI
import uvicorn
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
    effects[model.effect]()


if __name__=='__main__.py':
    uvicorn.run(app,port=3000)
