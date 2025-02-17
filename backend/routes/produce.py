from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.session import get_db
from db.models.produce import Produce
from schemas.produce import ProduceCreate, ProduceUpdate, ProduceOut
from typing import List

router = APIRouter(prefix="/produce", tags=["Produce"])

# Create produce
@router.post("/", response_model=ProduceOut)
def create_produce(produce: ProduceCreate, db: Session = Depends(get_db)):
    new_produce = Produce(**produce.dict())
    db.add(new_produce)
    db.commit()
    db.refresh(new_produce)
    return new_produce

# Get all produce
@router.get("/", response_model=List[ProduceOut])
def get_all_produce(db: Session = Depends(get_db)):
    return db.query(Produce).all()

# Get produce by ID
@router.get("/{produce_id}", response_model=ProduceOut)
def get_produce(produce_id: int, db: Session = Depends(get_db)):
    produce = db.query(Produce).filter(Produce.id == produce_id).first()
    if not produce:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produce not found")
    return produce

# Update produce
@router.put("/{produce_id}", response_model=ProduceOut)
def update_produce(produce_id: int, update_data: ProduceUpdate, db: Session = Depends(get_db)):
    db_produce = db.query(Produce).filter(Produce.id == produce_id).first()
    if not db_produce:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produce not found")

    for field, value in update_data.dict(exclude_unset=True).items():
        setattr(db_produce, field, value)

    db.commit()
    db.refresh(db_produce)
    return db_produce

# Delete produce
@router.delete("/{produce_id}")
def delete_produce(produce_id: int, db: Session = Depends(get_db)):
    db_produce = db.query(Produce).filter(Produce.id == produce_id).first()
    if not db_produce:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produce not found")

    db.delete(db_produce)
    db.commit()
    return {"message": "Produce deleted successfully"}

# Search produce by name
@router.get("/search/")
def search_produce(query: str, db: Session = Depends(get_db)):
    results = db.query(Produce).filter(Produce.product_name.ilike(f"%{query}%")).all()
    return results
