from fastapi import FastAPI
from app.routers import smart, usuarios

app = FastAPI()

app.include_router(usuarios.router)
app.include_router(smart.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}