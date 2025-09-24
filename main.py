from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")
def root():
    return {"Welcome to attendance page"}