from fastapi import FastAPI
from usuarios.urls import usuarios
from smart.urls import smart

app = FastAPI()

app.include_router(usuarios.router)
app.include_router(smart.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}