from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/names")
def read_root():
    return [{1:'Manuel'},{2:'EmX'}]




