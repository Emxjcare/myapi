from fastapi import FastAPI
import uvicorn
import requests

app = FastAPI()

@app.get("/")
def read_root():

    return {"message": "Bem Vindo a EmX Software Services!"}


@app.get("/capitulos")
def capitulos():
    return [
        {'id': 1, 'capitulo': 'Informatica New model'},
        {'id': 2, 'capitulo': 'Computador nova era'}
    ]

@app.get("/names")
def read_root():
    return [{1:'Manuel'},{2:'EmX'}]

