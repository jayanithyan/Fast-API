from typing import Optional
from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    price: float
    description: Optional[str] = None
    offer: Optional[float] = None
class ItemCreate(ItemBase):
    pass
class ItemUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None
    offer: Optional[float] = None