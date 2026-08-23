from fastapi import APIRouter, HTTPException
from schemas import ItemCreate, ItemUpdate, ItemResponse
from storage import load_items, save_items
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


@router.get("/", response_model=list[ItemResponse])
def get_items():
    return load_items()

@router.get("/search")
def search_items(name: str):
    items = load_items()

    return [
        item for item in items
        if name.lower() in item["name"].lower()
    ]
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


@router.delete("/{item_id}")
def delete_item(item_id: int):
    items = load_items()

    for item in items:
        if item["id"] == item_id:
            items.remove(item)
            save_items(items)

            return {"message": "Item deleted"}

    raise HTTPException(
        status_code=404,
        detail="Item not found"
    )


@router.put("/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, update: ItemUpdate):
    items = load_items()

    for item in items:
        if item["id"] == item_id:
            data = update.model_dump(exclude_unset=True)

            for key, value in data.items():
                item[key] = value

            save_items(items)

            return item

    raise HTTPException(
        status_code=404,
        detail="Item not found"
    )