from fastapi import APIRouter
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends
from app.database import get_db
from app.routers.crud import cabinets_crud
from app.schemas import CabinetCreate, Cabinet

router = APIRouter(prefix="/api/cabinets", tags=["cabinets"])

@router.get("/")
def read_cabinets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> List[Cabinet]:
    return cabinets_crud.get_cabinets(db, skip=skip, limit=limit)

@router.get("/{cabinet_id}")
def read_cabinet(cabinet_id: int, db: Session = Depends(get_db)) -> Cabinet:
    return cabinets_crud.get_cabinet(db, cabinet_id=cabinet_id)

@router.post("/")
def create_cabinet(cabinet: CabinetCreate, db: Session = Depends(get_db)) -> Cabinet:
    return cabinets_crud.create_cabinet(db=db, cabinet=cabinet)

@router.delete("/{cabinet_id}")
def delete_cabinet(cabinet_id: int, db: Session = Depends(get_db)) -> Cabinet:
    return cabinets_crud.delete_cabinet(db=db, cabinet_id=cabinet_id)

@router.put("/{cabinet_id}")
def update_cabinet(cabinet_id: int, cabinet: CabinetCreate, db: Session = Depends(get_db)) -> Cabinet:
    return cabinets_crud.update_cabinet(db=db, cabinet_id=cabinet_id, cabinet=cabinet)