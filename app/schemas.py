from pydantic import BaseModel
from typing import List, Optional

class ItemBase(BaseModel):
    name: str
    type: Optional[str] = None
    description: Optional[str] = None
    cabinet_id: int

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True

class CabinetBase(BaseModel):
    name: str

class CabinetCreate(CabinetBase):
    pass

class Cabinet(CabinetBase):
    id: int
    items: List[Item] = []

    class Config:
        orm_mode = True