from fastapi import APIRouter, HTTPException
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, status
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from app.routers.crud import cabinets_crud

router = APIRouter()

@router.get("/cabinets/", response_model=List[schemas.Cabinet])
def read_cabinets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return cabinets_crud.get_cabinets(db, skip=skip, limit=limit)

@router.get("/cabinets/{cabinet_id}", response_model=schemas.Cabinet)
def read_cabinet(cabinet_id: int, db: Session = Depends(get_db)):
    return cabinets_crud.get_cabinet(db, cabinet_id=cabinet_id)

@router.post("/cabinets/", response_model=schemas.Cabinet)
def create_cabinet(cabinet: schemas.CabinetCreate, db: Session = Depends(get_db)):
    return cabinets_crud.create_cabinet(db=db, cabinet=cabinet)

@router.delete("/cabinets/{cabinet_id}", response_model=schemas.Cabinet)
def delete_cabinet(cabinet_id: int, db: Session = Depends(get_db)):
    return cabinets_crud.delete_cabinet(db=db, cabinet_id=cabinet_id)

@router.put("/cabinets/{cabinet_id}", response_model=schemas.Cabinet)
def update_cabinet(cabinet_id: int, cabinet: schemas.CabinetCreate, db: Session = Depends(get_db)):
    return cabinets_crud.update_cabinet(db=db, cabinet_id=cabinet_id, cabinet=cabinet)