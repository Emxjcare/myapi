from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bem Vindo a EmX Software Services!"}
@app.get("/capitulos")
def capitulos():
    return [
        {
            'id' = 1,
            'capitulo' = 'Informatica'
        },
        {
            'id' = 2,
            'capitulo' = 'Computador'
        }
        
    ]

@app.get("/names")
def read_root():
    return [{1:'Manuel'},{2:'EmX'}]






