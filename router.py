from fastapi import APIRouter
from schemas import ItemCreate, ItemResponse
from storage import load_items, save_items
from datetime import datetime
from schemas import ItemCreate, ItemResponse
from datetime import datetime
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/items", tags=["Items"])


@router.get("/health")
def items_health():
    return {"status": "items router active"}
@router.post("/", response_model=ItemResponse)
items = []
def create_item(item: ItemCreate):
    items = load_items()
    
    new_item = {
        "id": len(items) + 1,
        "name": item.name,
        "price": item.price,
        "description": item.description,
        "offer": item.offer,
        "created_at": datetime.now().isoformat()
    }
    items.append(new_item)

    return new_item
@router.post("/", response_model=ItemResponse)
def create_item(item: ItemCreate):
    new_item = {
        "id": 1,
        "name": item.name,
        "price": item.price,
        "description": item.description,
        "offer": item.offer,
        "created_at": datetime.now().isoformat()
    }

    return new_item

@router.get("/", response_model=list[ItemResponse])
def get_items():
    return items

@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item

    raise HTTPException(
        status_code=404,
        detail="Item not found"
    )
@router.delete("/{item_id}")
def delete_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            items.remove(item)
            return {"message": "Item deleted"}

    raise HTTPException(
        status_code=404,
        detail="Item not found"
    )