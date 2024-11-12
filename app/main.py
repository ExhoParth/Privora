from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/generate")
def generate():
    return {"response": "-"}
