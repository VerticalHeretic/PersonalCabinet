from sqlalchemy.orm import Session
from fastapi import HTTPException
from app import models, schemas

def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(name=item.name, type=item.type, description=item.description, cabinet_id=item.cabinet_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return db_item

def update_item(db: Session, item_id: int, item: schemas.ItemCreate):
    db_item = db.query(models.Item).filter(models.Cabinet.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Cabinet not found")

    db_item.name = item.name
    db_item.type = item.type
    db_item.description = item.description

    db.commit()
    db.refresh(db_item)
    return db_item