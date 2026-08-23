from fastapi import APIRouter

router = APIRouter(prefix="/items", tags=["Items"])


@router.get("/health")
def items_health():
    return {"status": "items router active"}