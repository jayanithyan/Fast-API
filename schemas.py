from typing import Optional
from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    name: str=Field(min_length=2, max_length=100)
    price: float = Field(gt=0)
    description: Optional[str] = None
    offer: Optional[float] = None


class ItemCreate(ItemBase):
    pass


class ItemUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None
    offer: Optional[float] = None


class ItemResponse(ItemBase):
    id: int
    created_at: str