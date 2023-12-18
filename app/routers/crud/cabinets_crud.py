from sqlalchemy.orm import Session
from fastapi import HTTPException
from app import models, schemas

def get_cabinet(db: Session, cabinet_id: int):
    return db.query(models.Cabinet).filter(models.Cabinet.id == cabinet_id).first()

def get_cabinets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Cabinet).offset(skip).limit(limit).all()

def create_cabinet(db: Session, cabinet: schemas.CabinetCreate):
    db_cabinet = models.Cabinet(name=cabinet.name)
    db.add(db_cabinet)
    db.commit()
    db.refresh(db_cabinet)
    return db_cabinet

def delete_cabinet(db: Session, cabinet_id: int):
    db_cabinet = db.query(models.Cabinet).filter(models.Cabinet.id == cabinet_id).first()
    if db_cabinet is None:
        raise HTTPException(status_code=404, detail="Cabinet not found")
    db.delete(db_cabinet)
    db.commit()
    return db_cabinet

def update_cabinet(db: Session, cabinet_id: int, cabinet: schemas.CabinetCreate):
    db_cabinet = db.query(models.Cabinet).filter(models.Cabinet.id == cabinet_id).first()
    if db_cabinet is None:
        raise HTTPException(status_code=404, detail="Cabinet not found")
    db_cabinet.name = cabinet.name
    db.commit()
    db.refresh(db_cabinet)
    return db_cabinet