from fastapi import FastAPI
from router import router as items_router

app = FastAPI(title="Item Store API", version="1.0.0")

app.include_router(items_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
@router.get("/", response_model=list[ItemResponse])
def get_items():
    return load_items()