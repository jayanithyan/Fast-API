from fastapi import FastAPI
from routes import router as items_router

app = FastAPI(title="Item Store API", version="1.0.0")

app.include_router(items_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}