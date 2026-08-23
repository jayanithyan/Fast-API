from fastapi import APIRouter
from schemas import ItemCreate, ItemResponse
from storage import load_items, save_items
from datetime import datetime
from schemas import ItemCreate, ItemResponse
from datetime import datetime

router = APIRouter(prefix="/items", tags=["Items"])


@router.get("/health")
def items_health():
    return {"status": "items router active"}
@router.post("/", response_model=ItemResponse)
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
    save_items(items)

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