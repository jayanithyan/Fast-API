from fastapi import FastAPI
from router import router as items_router
from fastapi import HTTPException
app = FastAPI(title="Item Store API", version="1.0.0")

app.include_router(items_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
@router.get("/", response_model=list[ItemResponse])
def get_items():
    return load_items()
@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: int):
    items = load_items()

    for item in items:
        if item["id"] == item_id:
            return item

    raise HTTPException(
        status_code=404,
        detail="Item not found"
    )