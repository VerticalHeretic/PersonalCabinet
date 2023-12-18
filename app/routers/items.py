from fastapi import APIRouter
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends
from app.database import get_db
from app.routers.crud import items_crud
from app.schemas import ItemCreate, Item

router = APIRouter(prefix="/api/items", tags=["items"])

@router.get("/")
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> List[Item]:
    return items_crud.get_items(db, skip=skip, limit=limit)

@router.get("/{cabinet_id}")
def read_item(item_id: int, db: Session = Depends(get_db)) -> Item:
    return items_crud.get_item(db, item_id=item_id)

@router.post("/")
def create_item(item: ItemCreate, db: Session = Depends(get_db)) -> Item:
    return items_crud.create_item(db=db, item=item)

@router.delete("/{cabinet_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    return items_crud.delete_item(db=db, item_id=item_id)

@router.put("/{cabinet_id}")
def update_item(item_id: int, item: ItemCreate, db: Session = Depends(get_db)) -> Item:
    return items_crud.update_item(db=db, item_id=item_id, item=item)