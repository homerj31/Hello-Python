from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Hola Oscar este es tu primer FastAPI!"

@app.get("/url")
async def url():
    return {"url" : "www.marca.es"}

