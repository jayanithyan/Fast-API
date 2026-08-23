from typing import Optional
from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    name: str
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