from fastapi import FastAPI
from router import router as items_router

app = FastAPI(
    title="Item Store API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {"Hello": "World"}


app.include_router(items_router)
@app.get("/info")
def api_info():
    return {
        "name": "Item Store API",
        "version": "1.0.0"
    }