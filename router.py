from fastapi import APIRouter, HTTPException, Query
from schemas import ItemCreate, ItemUpdate, ItemResponse
from storage import load_items, save_items
from datetime import datetime

router = APIRouter(prefix="/items", tags=["Items"])


@router.post("/", response_model=ItemResponse)
def create_item(item: ItemCreate):
    items = load_items()

    new_id = max([item["id"] for item in items], default=0) + 1

    new_item = {
        "id": new_id,
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
        item
        for item in items
        if name.lower() in item["name"].lower()
    ]


@router.get("/filter")
def filter_items(max_price: float):
    items = load_items()

    return [
        item
        for item in items
        if item["price"] <= max_price
    ]


@router.get("/sort")
def sort_items(order: str = "asc"):
    items = load_items()

    return sorted(
        items,
        key=lambda item: item["price"],
        reverse=order == "desc"
    )


@router.get("/count")
def count_items():
    items = load_items()

    return {"count": len(items)}


@router.get("/average-price")
def average_price():
    items = load_items()

    if not items:
        return {"average_price": 0}

    average = sum(item["price"] for item in items) / len(items)

    return {"average_price": round(average, 2)}


@router.get("/page")
def get_items_page(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=50)
):
    items = load_items()

    return items[skip:skip + limit]


@router.get("/health")
def items_health():
    items = load_items()

    return {
        "status": "healthy",
        "items": len(items)
    }


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