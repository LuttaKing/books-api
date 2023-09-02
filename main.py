from fastapi import FastAPI

app = FastAPI()

books = ['book1','book2']

@app.get("/")
def rea():
    return books